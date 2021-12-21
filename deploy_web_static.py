#!/usr/bin/python3
"""
script based on set_static_web.sh that distributes an
archive to web servers
"""

from fabric.api import put, run, env
from os.path import exists


def do_deploy(archive_path):
    """destributes an archive to web server"""
    if exists(archive_path):
        return False
    try:
        files = archive_path.split("/")[-1]
        exten = files.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, exten))
        run('tar -xzf /tmp/{} -C {}{}/'.format(files, path, exten))
        run('rm /tmp/{}'.format(files))
        run('mv {0][1]/web_static/* {0}{1}/'.format(path, exten))
        run('rm -rf {}{}/web_static'.format(path, exten))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, exten))
        return True
    except:
        return False
