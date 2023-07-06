#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of this repo
"""
from fabric.api import local
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
    except Exception:
        return None