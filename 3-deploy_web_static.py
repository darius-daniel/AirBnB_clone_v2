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
env.password = "~/.ssh/alx_ssh_key"


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
        print("Packing web_static to {}".format(tgz_path))
        local("tar -cvzf {} web_static".format(tgz_path))
        size = os.path.getsize(tgz_path)
        print("web_static packed: {} -> {}Bytes".format(tgz_path, size))
        return tgz_path
    except Exception:
        return False


def do_deploy(archive_path):
    """
    A function to distribute an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_name = archive_path.split('/')[-1].split('.')[0]
        releases = "/data/web_static/releases/{}".format(archive_name)
        symbolic_ln = "/data/web_static/current"

        temp_path = '/tmp/{}'.format(archive_name)
        run("mkdir -p {}".format(releases))
        run("tar -xzf {}.tgz -C {}".format(temp_path, releases))
        run("rm {}.tgz".format(temp_path))
        run("cp -r {}/web_static/* {}/".format(releases, releases))
        run("rm -rf {}/web_static".format(releases))
        run("rm -rf {}".format(symbolic_ln))
        run("ln -s {}/ {}".format(releases, symbolic_ln))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    Deploys a new version to web servers
    """
    archive_path = do_pack()
    print(archive_path)
    if archive_path is None:
        return False

    return do_deploy(archive_path)
