#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def createcommand(command):
    finished_command = []
    finished_command = command.split(" ")

request_temp = '''/opt/vc/bin/vcgencmd measure_temp | sed 's/temp=//g' | sed "s/'.*//g"'''

temp = subprocess.Popen(request_temp.split(" "), stdout=subprocess.PIPE)
output = temp.communicate()[0]
