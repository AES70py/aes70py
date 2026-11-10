AES70py Project
==========

Pure Python 3 controller implementation of the AES70 standard.

Current features
==============

1. 100 control classes supported
2. Near complete coverage of Open Specification of AES70 2024
3. Asynchronous communication
4. TCP and WebSocket protocol connection support
5. Basic subscription support

More features are in development, so stay tuned for updates by joining our LinkedIn group:

https://www.linkedin.com/groups/9859354/

Installation
============

AES70py is a pure python library that has 2 external dependencies: promise and mdns-sd. To install it just use `pip`...

## Run Utility
In the `examples/tools` folder `run.sh` is a helper bash script for quickly testing python scripts. Use `run.sh` inside a new folder alongside the desired python example(s) scripts for installing the environment and running the python.

1. Make a new directory `mkdir`, then copy the python script and `run.sh` into that new directory, (myproject).
2. You may need to `chmod +x` on run.sh
3. Run the setup project:
```
cd myproject/
./run.sh --help
./run.sh --install --script-name <script_name>.py
./run.sh --status
./run.sh --list
./run.sh
```
4. It is possible to have multiple scripts, but for now it is a helper for fast tracking the manual instructions below.

## Manual Steps for testing examples
In your terminal use the following (this sets up a virtual environment to keep all of the python libraries 
in a private location):

```
python3 -m venv aes70-project
```
```
cd aes70-project
```
```
source bin/activate
```
```
python3 -m pip install aes70py
```

Copy an example, such as  examples/connect_toggle_mute.py from our github repository (https://github.com/AES70py/aes70py)
 to the aes70-project directory.

Modify it to suit your device ip address and port. 

Then run:

```
python3 connect_toggle_mute.py
```

Post any and all requests to the issues, many thanks.

The AES70py Team
