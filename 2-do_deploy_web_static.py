#!/usr/bin/python3
from fabric.api import put, run, local, env
import os
import fabric.api as api


env.hosts = ["52.86.204.80", "34.202.158.153"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """check and run locally"""

    """Fabric script that distributes
    an archive to your web server"""

    if not os.path.exists(archive_path):
        return False
    try:
        tgzfile_name = archive_path.split("/")[-1]
        fileName_not_ext = tgzfile_name.split(".")[0]
        old_path_name = "/data/web_static/releases/{}/web_static".format(
            fileName_not_ext)
        new_path = '/data/web_static/releases/{}'.format(fileName_not_ext)
        curr_path = 'data/web_static/current'

        '''first run and deploy locally'''
        run_locally = os.getenv("run_locally", None)
        if run_locally is None:
            api.local(f'sudo mkdir -p {new_path}')
            api.local(f'sudo tar -zxf {archive_path} -C {new_path}')
            api.local(f'sudo rm -rfR {curr_path}')
            api.local(f'ln -s {new_path} {curr_path}')
            os.environ['run_locally'] = "True"
        print('locally deployed successfully')

        '''deploy to the server remotely'''
        put(archive_path, '/tmp/')
        run(f'mkdir -p {new_path}')
        run(f'tar -zxf {archive_path} -C {new_path}')
        run(f'rm /tmp/{tagzfile_name}')
        run(f'rm -rfR {curr_path}')
        run(f'ln -s {new_path} {curr_path}')
        print('remotely deployed to their server successfully')

        return True
    except Exception as e:
        return False
