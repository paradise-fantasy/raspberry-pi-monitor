#!/usr/bin/python
# -*- coding: utf-8 -*-
debug = 1


import subprocess

get_load = "snmpwalk -c public -v 2c localhost:161 .1.3.6.1.4.1.2021.10.1.3"
get_temp = "/opt/vc/bin/vcgencmd measure_temp"

get_load_ubuntu = "snmpwalk -c public -v 2c localhost:161 .1.3.6.1"

def command(command):
    temp = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)
    output = temp.communicate()[0]
    return output


def main():
    if debug:
        print(command(get_load_ubuntu))
    else:
        print command(get_load)
        print command(get_temp)

if __name__ == "__main__":
    main()
