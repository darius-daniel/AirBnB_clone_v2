#!/usr/bin/python3
"""
A Fabric script that distributes an archive to web servers
"""
from fabric.api import local
from fabric.api import put
import datetime
import os


def do_pack():
    """
    A function that generates a .tgz archive from the contents of the
    web_static directory
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        present = datetime.datetime.now()
        tgz_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
                present.year,
                present.month,
                present.day,
                present.hour,
                present.minute,
                present.second
        )
        print(tgz_path)
        local("tar -cvzf {} web_static".format(tgz_path))
        return tgz_path
    except Exception as e:
        return e


def do_deploy(archive_path):
    """
    A function to distribute an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp/', use_sudo=True)

    dest_dir = archive_path.split('/')[-1].split('.')[0]
    print(dest_dir)
    releases = "/data/web_static/releases/{}".format(dest_dir)
    symbolic_ln = "/data/web_static/current"

    local("tar -xf archive_path -C {}".format(releases))
    local("rm archive_path")

    local("rm {}".format(symbolic_ln))
    local("ln -s {} {}".format(releases, symbolic_ln))
