#!/usr/bin/python3
"""
Fab file to deploy static web on server
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.236.43.198', '54.175.134.96']


def do_deploy(arch):
    """distributes an archive to the web servers"""
    if exists(arch) is False:
        return False
    try:
        file_num = arch.split("/")[-1]
        no_exit = file_num.split(".")[0]
        path = "/data/web_static/releases/"
        put(arch, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_exit))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_num, path, no_exit))
        run('rm /tmp/{}'.format(file_num))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_exit))
        run('rm -rf {}{}/web_static'.format(path, no_exit))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_exit))
        return True
    except:
        return False
