#!/usr/bin/python3
"""
This is a fabric script that compress a file to
generate archive in tgz format
how to execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """

    time = datetime.now()
    arch = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(arch))
    if create is not None:
        return arch
    else:
        return None
