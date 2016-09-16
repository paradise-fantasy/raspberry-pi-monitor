#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

request_temp = '''/opt/vc/bin/vcgencmd measure_temp | sed 's/temp=//g' | sed "s/'.*//g"'''

temp = subprocess.Popen(request_temp)

print temp

