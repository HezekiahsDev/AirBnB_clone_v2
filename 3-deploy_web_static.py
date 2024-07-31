#!/usr/bin/python3
"""
Fabric file to create and deploy static files

usage: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.236.43.198', '54.175.134.96']


def do_pack():
    """compress into tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(arch):
    """distribute archives to webservers"""
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


def deploy():
    """create and share archives between servers"""
    arch = do_pack()
    if arch is None:
        return False
    return do_deploy(arch)
