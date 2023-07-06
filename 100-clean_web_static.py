#!/usr/bin/python3
""" A clean-up script
"""
from fabric.api import *

env.hosts = ["35.153.19.179", "34.201.174.149"]
env.user = "ubuntu"
env.password = "~/.ssh/alx_ssh_key"

def do_clean(number=0):
    """ A clean-up function
    """
    if number == 0 or number == 1:
        to_keep = 1
    else:
        to_keep = 2
        
    local('ls -t versions | tail -n +{} | xargs rm -rf'.format(to_keep))
    releases = "/data/web_static/releases"
    run("ls -t {} | tail -n +{} | xargs rm -rf".format(releases, to_keep))
