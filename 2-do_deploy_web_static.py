#!/usr/bin/python3
"""
A Fabric script that distributes an archive to web servers
"""
from fabric.api import *
import datetime
import os


env.hosts = [
    '35.153.19.179',
    '34.201.174.149'
]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    A function to distribute an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_name = archive_path.split('/')[-1].split('.')[0]
        print(archive_name)
        releases = "/data/web_static/releases/{}".format(archive_name)
        symbolic_ln = "/data/web_static/current"

        temp_path = '/tmp/{}'.format(archive_name)
        run("mkdir -p {}".format(releases))
        run("tar -xf {}.tgz -C {}".format(temp_path, releases))
        run("rm -rf archive_path")

        run("rm -rf {}".format(symbolic_ln))
        run("ln -s {} {}".format(releases, symbolic_ln))
        print("New version deployed!")
        return True
    except:
        return False

