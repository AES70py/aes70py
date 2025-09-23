AES70py Project
==========

Pure Python 3 controller implementation of the AES70 standard.

Current features
==============

1. 100 control classes supported
2. Near complete coverage of Open Specification of AES70 2018
3. Asynchronous communication
4. TCP protocol connection support

Installation
============

AES70py is a pure python library that has no external dependencies. To install it just use `pip`...

## Steps
In your terminal use the following:

```
python3 -m venv aes70-project
cd aes70-project
source bin/activate
python3 -m pip install https://github.com/AES70py/aes70py/releases/download/1.0.2/aes70py-1.0.2-py3-none-any.whl
```
Copy the examples/connect_toggle_mute.py into the aes70-project directory, run:

```
python3 connect_toggle_mute.py
```

Post any and all requests to the issues, many thanks.

AES70py Team