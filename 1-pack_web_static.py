#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """ Create the versions folder if it doesn't exist """
    if not os.path.exists("versions"):
        os.mkdir("versions")
    """ Create the archive name with the format web_static_
    <year><month><day><hour><minute><second>.tgz """
    cur_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_%s.tgz" % cur_time

    # Compress the contents of the web_static folder into the archive
    try:
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))
        archive_size = os.stat(archive_name).st_size
        print("web_static packed:
              {} -> {} Bytes".format(archive_name, archive_size))
    except Exception:
        archive_name = None
    return archive_name
