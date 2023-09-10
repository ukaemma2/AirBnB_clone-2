#!/usr/bin/python3
"""
A Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


"""The list of host servers and credentials."""
env.hosts = ["52.86.204.80", "34.202.158.153"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

@runs_once
def do_pack():
    """ Create the versions folder if it doesn't exist """
    if not os.path.exists("versions"):
        os.mkdir("versions")

    """ Create the archive name with the format web_static_
    <year><month><day><hour><minute><second>.tgz """
    cur_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_%s.tgz" %cur_time

    # Compress the contents of the web_static folder into the archive
    try:
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))
        archive_size = os.stat(archive_name).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_name, archive_size))
    except Exception as e:
        print("Error packing web_static:", str(e))
        archive_name = None
    return archive_name


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        print(f"Archive not found: {archive_path}")
        return False

    # Upload archive
    put(archive_path, '/tmp/')

    # Create target dir
    timestamp = archive_path[-18:-4]
    run('sudo mkdir -p /data/web_static/releases/web_static_{}/'.format(timestamp))

    # Uncompress archive and delete .tgz
    run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/releases/web_static_{}/'
        .format(timestamp, timestamp))

    # Remove archive
    run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

    # Move contents into host web_static
    run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
        /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

    # Remove extraneous web_static dir
    run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'.format(timestamp))

    # Delete pre-existing sym link
    run('sudo rm -rf /data/web_static/current')

    # Re-establish symbolic link
    run('sudo ln -s /data/web_static/releases/web_static_{}/ /data/web_static/current'.format(timestamp))

    print("New version deployed!")
    return True

