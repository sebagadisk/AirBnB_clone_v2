#!/usr/bin/python3
"""
script based on deploy_web_static.py that creates and
distributes an archive to web server
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['34.44.127.228', '34.44.206.195']


def do_pach():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        files = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} {} web_static".format(file_name))
        return files
    except:
        return None


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


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
