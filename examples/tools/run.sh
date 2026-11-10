#!/usr/bin/env bash
# aes70py runner for this folder. Works in Linux/macOS Terminal and Windows Git Bash.

set -euo pipefail

cd "$(dirname "$0")"

CONFIG="project.conf"
ACTION=""
SCRIPT_NAME=""
URL=""
PORT=""
UPDATE_DEPS=""

usage() {
  cat <<'EOF'
aes70py runner for this folder. You do not need to activate a virtual environment.

  ./run.sh --install --script-name FILE.py
      Create the private Python environment if needed, install aes70py the first time, and install FILE.py.
      If aes70py is already installed, the environment is left as it is.

  ./run.sh --update-deps
      Refresh pip and aes70py in the existing environment.

  ./run.sh --install --script-name FILE.py --update-deps
      Register FILE.py and refresh pip and aes70py in the same step.

  ./run.sh
      Run the only installed script.

  ./run.sh --script-name FILE.py
      Run that installed script when more than one is installed.

  ./run.sh --url HOST --port PORT
      Optional, with a run. HOST and PORT are split, for example
      ./run.sh --url aes70x.net --port 1058
      Both are passed through to the script. HOST may be a hostname or ws://hostname.
      If you leave both off, the script uses the address written inside it.

      In the .py file, read the two arguments, then connect in one line:
      url, port = sys.argv[sys.argv.index("--url") + 1], sys.argv[sys.argv.index("--port") + 1]
      ws_connection.connect(host=urlparse(url).hostname or url, port=int(port))

  ./run.sh --list
      Show installed scripts.

  ./run.sh --status
      Show Python, the environment, the aes70py version, and installed scripts.

  ./run.sh --remove --script-name FILE.py
      Forget a script. Does not delete the .py file or the environment.

  ./run.sh --help
EOF
}

die() {
  echo "$1" >&2
  exit 1
}

set_action() {
  if [ -n "$ACTION" ] && [ "$ACTION" != "$1" ]; then
    echo "Use only one of --install, --list, --status, --remove, or --help." >&2
    echo >&2
    usage
    exit 1
  fi
  ACTION="$1"
}

while [ $# -gt 0 ]; do
  case "$1" in
    --help|-h)
      set_action help
      ;;
    --install)
      set_action install
      ;;
    --list)
      set_action list
      ;;
    --status)
      set_action status
      ;;
    --remove)
      set_action remove
      ;;
    --update-deps)
      UPDATE_DEPS=1
      ;;
    --script-name)
      if [ $# -lt 2 ]; then
        die "--script-name needs a file name, for example: --script-name connect_ws_adjust_limit.py"
      fi
      shift
      SCRIPT_NAME="$1"
      ;;
    --url)
      if [ $# -lt 2 ]; then
        die "--url needs a host, for example: --url aes70x.net"
      fi
      shift
      URL="$1"
      ;;
    --port)
      if [ $# -lt 2 ]; then
        die "--port needs a port number, for example: --port 1058"
      fi
      shift
      PORT="$1"
      ;;
    *)
      echo "Unknown option: $1" >&2
      echo >&2
      usage
      exit 1
      ;;
  esac
  shift
done

if [ -z "$ACTION" ]; then
  if [ -n "$UPDATE_DEPS" ]; then
    ACTION="update-deps"
  else
    ACTION="run"
  fi
fi

if [ -n "$URL" ] && [ -z "$PORT" ]; then
  die "--url needs --port as well. Example: ./run.sh --url aes70x.net --port 1058"
fi
if [ -n "$PORT" ] && [ -z "$URL" ]; then
  die "--port needs --url as well. Example: ./run.sh --url aes70x.net --port 1058"
fi

python_is_new_enough() {
  "$@" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 1)'
}

discover_base_python() {
  BASE_PYTHON=()
  if command -v python3 >/dev/null 2>&1 && python_is_new_enough python3; then
    BASE_PYTHON=(python3)
    return 0
  fi
  if command -v python >/dev/null 2>&1 && python_is_new_enough python; then
    BASE_PYTHON=(python)
    return 0
  fi
  if command -v py >/dev/null 2>&1 && python_is_new_enough py -3; then
    BASE_PYTHON=(py -3)
    return 0
  fi
  die "aes70py needs Python 3.12 or newer. Install it, then run this again."
}

venv_python() {
  if [ -x venv/bin/python ]; then
    echo "venv/bin/python"
    return 0
  fi
  if [ -f venv/Scripts/python.exe ]; then
    echo "venv/Scripts/python.exe"
    return 0
  fi
  return 1
}

require_simple_name() {
  case "$1" in
    -*)
      die "Script names cannot start with '-'. Example: --script-name connect_ws_adjust_limit.py"
      ;;
    ""|*/*|*\\*|*" "*|*$'\t'*)
      die "Use a file name in this folder, not a path. Example: --script-name connect_ws_adjust_limit.py"
      ;;
    *.py) ;;
    *)
      die "Script names must end in .py. Example: --script-name connect_ws_adjust_limit.py"
      ;;
  esac
}

read_scripts() {
  SCRIPTS=()
  [ -f "$CONFIG" ] || return 0
  while IFS= read -r line || [ -n "$line" ]; do
    line="${line%$'\r'}"
    case "$line" in
      ""|\#*) continue ;;
      script\ *)
        SCRIPTS+=("${line#script }")
        ;;
    esac
  done < "$CONFIG"
  if [ "${#SCRIPTS[@]}" -eq 0 ]; then
    return 0
  fi
  local name
  for name in "${SCRIPTS[@]}"; do
    require_simple_name "$name"
  done
}

script_is_known() {
  local name="$1"
  local existing
  read_scripts
  if [ "${#SCRIPTS[@]}" -eq 0 ]; then
    return 1
  fi
  for existing in "${SCRIPTS[@]}"; do
    if [ "$existing" = "$name" ]; then
      return 0
    fi
  done
  return 1
}

write_new_config() {
  cat > "$CONFIG" <<'EOF'
# One filename per line. If exactly one is listed, ./run.sh runs it.
# Device addresses belong in the Python file, not here.
EOF
  printf 'script %s\n' "$1" >> "$CONFIG"
}

add_script() {
  local name="$1"
  if [ ! -f "$CONFIG" ]; then
    write_new_config "$name"
    return 0
  fi
  if script_is_known "$name"; then
    echo "$name is already installed."
    return 0
  fi
  printf 'script %s\n' "$name" >> "$CONFIG"
}

remove_script() {
  local name="$1"
  local tmp found=0 line
  if [ ! -f "$CONFIG" ]; then
    die "$name is not installed. Nothing was removed."
  fi
  tmp="$(mktemp)"
  while IFS= read -r line || [ -n "$line" ]; do
    line="${line%$'\r'}"
    if [ "$line" = "script $name" ]; then
      found=1
      continue
    fi
    printf '%s\n' "$line" >> "$tmp"
  done < "$CONFIG"
  if [ "$found" -eq 0 ]; then
    rm -f "$tmp"
    die "$name is not installed. Nothing was removed."
  fi
  mv "$tmp" "$CONFIG"
  echo "Forgot $name. The .py file is still in this folder."
}

list_py_files() {
  local found=0 name
  for name in *.py; do
    if [ -f "$name" ]; then
      echo "  $name"
      found=1
    fi
  done
  if [ "$found" -eq 0 ]; then
    echo "  (none yet)"
  fi
}

show_list() {
  local count name
  read_scripts
  count="${#SCRIPTS[@]}"
  if [ "$count" -eq 0 ]; then
    echo "No scripts installed."
    return 0
  fi
  echo "Scripts:"
  if [ "$count" -eq 1 ]; then
    echo "  ${SCRIPTS[0]}  (default)"
    return 0
  fi
  for name in "${SCRIPTS[@]}"; do
    echo "  $name"
  done
}

show_status() {
  local py version
  if py="$(venv_python)"; then
    version="$("$py" -c 'import sys; print(sys.version.split()[0])')"
    echo "Python: $version"
    echo "Environment: ready ($py)"
    if "$py" -m pip show aes70py >/dev/null 2>&1; then
      echo "aes70py: $("$py" -m pip show aes70py | awk -F': ' '/^Version:/{print $2}')"
    else
      echo "aes70py: not installed"
    fi
  else
    echo "Python: not set up yet"
    echo "Environment: missing"
    echo "aes70py: not installed"
  fi
  show_list
}

ensure_venv() {
  local py
  if py="$(venv_python)"; then
    if "$py" -m pip --version >/dev/null 2>&1; then
      echo "$py"
      return 0
    fi
    echo "Removing environment that has no pip..." >&2
    rm -rf venv
  fi
  discover_base_python
  if ! "${BASE_PYTHON[@]}" -c 'import ensurepip' >/dev/null 2>&1; then
    die "Python cannot install pip into a new environment. On Ubuntu run: sudo apt install python3-venv"
  fi
  echo "Creating the private Python environment..." >&2
  if ! "${BASE_PYTHON[@]}" -m venv venv; then
    rm -rf venv
    die "The environment was not created. On Ubuntu run: sudo apt install python3-venv"
  fi
  if ! py="$(venv_python)" || ! "$py" -m pip --version >/dev/null 2>&1; then
    rm -rf venv
    die "The environment was not created. On Ubuntu run: sudo apt install python3-venv"
  fi
  echo "$py"
}

aes70_installed() {
  "$1" -m pip show aes70py >/dev/null 2>&1
}

install_aes70() {
  local py="$1"
  if [ -n "$UPDATE_DEPS" ]; then
    echo "Updating pip and aes70py..."
    "$py" -m pip install --upgrade pip
    "$py" -m pip install --upgrade aes70py
    return 0
  fi
  echo "Installing aes70py from PyPI..."
  "$py" -m pip install aes70py
}

cmd_install() {
  local py
  if [ -z "$SCRIPT_NAME" ]; then
    echo "--install needs --script-name. Python files in this folder:" >&2
    list_py_files >&2
    echo "Example:" >&2
    echo "  ./run.sh --install --script-name connect_ws_adjust_limit.py" >&2
    exit 1
  fi
  if [ -n "$URL" ] || [ -n "$PORT" ]; then
    die "--url and --port are only used when running a script. Leave them off for --install."
  fi
  require_simple_name "$SCRIPT_NAME"
  if [ ! -f "$SCRIPT_NAME" ]; then
    die "$SCRIPT_NAME is not in this folder. Copy it here, then install it."
  fi
  py="$(ensure_venv)"
  if [ -n "$UPDATE_DEPS" ] || ! aes70_installed "$py"; then
    install_aes70 "$py"
  else
    echo "aes70py is already installed. Leaving the environment as it is."
    echo "To refresh pip and aes70py, run: ./run.sh --update-deps"
  fi
  add_script "$SCRIPT_NAME"
  echo
  echo "Installed $SCRIPT_NAME."
  read_scripts
  if [ "${#SCRIPTS[@]}" -eq 1 ]; then
    echo "Run it with:"
    echo "  ./run.sh"
  else
    echo "Run it with:"
    echo "  ./run.sh --script-name $SCRIPT_NAME"
  fi
}

choose_script() {
  local count
  read_scripts
  count="${#SCRIPTS[@]}"
  if [ "$count" -eq 0 ]; then
    echo "No scripts installed yet. Put a .py file in this folder, then:" >&2
    echo "  ./run.sh --install --script-name your_script.py" >&2
    if [ -n "$SCRIPT_NAME" ]; then
      echo "Python files in this folder:" >&2
      list_py_files >&2
    fi
    exit 1
  fi
  if [ -z "$SCRIPT_NAME" ]; then
    if [ "$count" -eq 1 ]; then
      SCRIPT_NAME="${SCRIPTS[0]}"
      return 0
    fi
    echo "More than one script is installed. Pick one:" >&2
    local name
    for name in "${SCRIPTS[@]}"; do
      echo "  ./run.sh --script-name $name" >&2
    done
    exit 1
  fi
  require_simple_name "$SCRIPT_NAME"
  if ! script_is_known "$SCRIPT_NAME"; then
    die "$SCRIPT_NAME is not installed. Run: ./run.sh --install --script-name $SCRIPT_NAME"
  fi
}

run_python() {
  local py="$1"
  shift
  local log code missing
  log="$(mktemp)"
  set +e
  "$py" -- "$@" 2>&1 | tee "$log"
  code=$?
  set -e
  missing=""
  if grep -q "not in list" "$log"; then
    missing="$(grep -oE 'index\("(--[^"]+)"\)|index\('"'"'(--[^'"'"']+)'"'"'\)' "$log" | grep -oE -- '--[^"'"'"']+' | sort -u | tr '\n' ' ' || true)"
  fi
  if [ "$code" -ne 0 ] && [ -n "$missing" ]; then
    echo "Missing script arguments: $missing" >&2
    echo "Example: ./run.sh --url aes70x.net --port 1058" >&2
  elif [ "$code" -ne 0 ] && grep -q "not in list" "$log"; then
    echo "Missing script arguments." >&2
    echo "Example: ./run.sh --url aes70x.net --port 1058" >&2
  elif [ "$code" -ne 0 ] && grep -q "list index out of range" "$log"; then
    echo "Missing script arguments. A value after --url or --port was not provided." >&2
    echo "Example: ./run.sh --url aes70x.net --port 1058" >&2
  fi
  rm -f "$log"
  exit "$code"
}

cmd_run() {
  local py
  if ! py="$(venv_python)"; then
    die "No aes70py environment yet. Run: ./run.sh --install --script-name your_script.py"
  fi
  choose_script
  if [ ! -f "$SCRIPT_NAME" ]; then
    die "$SCRIPT_NAME is registered but the file is missing from this folder."
  fi
  if [ -n "$URL" ]; then
    run_python "$py" "$SCRIPT_NAME" --url "$URL" --port "$PORT"
  fi
  run_python "$py" "$SCRIPT_NAME"
}

cmd_update_deps() {
  local py
  if [ -n "$SCRIPT_NAME" ] || [ -n "$URL" ] || [ -n "$PORT" ]; then
    die "--update-deps does not take --script-name, --url, or --port. To register a script as well, add --install."
  fi
  if ! py="$(venv_python)"; then
    die "No aes70py environment yet. Run: ./run.sh --install --script-name your_script.py"
  fi
  install_aes70 "$py"
}

cmd_remove() {
  if [ -z "$SCRIPT_NAME" ]; then
    die "--remove needs --script-name. Example: ./run.sh --remove --script-name connect_ws_adjust_limit.py"
  fi
  if [ -n "$URL" ] || [ -n "$PORT" ]; then
    die "--url and --port are only used when running a script."
  fi
  require_simple_name "$SCRIPT_NAME"
  remove_script "$SCRIPT_NAME"
}

case "$ACTION" in
  help|list|status|remove|run)
    if [ -n "$UPDATE_DEPS" ]; then
      die "--update-deps only works alone or with --install."
    fi
    ;;
esac

case "$ACTION" in
  help)
    usage
    ;;
  install)
    cmd_install
    ;;
  update-deps)
    cmd_update_deps
    ;;
  run)
    cmd_run
    ;;
  list)
    if [ -n "$SCRIPT_NAME" ] || [ -n "$URL" ] || [ -n "$PORT" ]; then
      die "--list does not take --script-name, --url, or --port."
    fi
    show_list
    ;;
  status)
    if [ -n "$SCRIPT_NAME" ] || [ -n "$URL" ] || [ -n "$PORT" ]; then
      die "--status does not take --script-name, --url, or --port."
    fi
    show_status
    ;;
  remove)
    cmd_remove
    ;;
esac
