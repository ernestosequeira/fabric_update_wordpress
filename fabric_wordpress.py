#!/usr/bin/env python
from fabric.api import (
    env,
    sudo,
)
from fabric.colors import (
    green,
)

env.hosts = ['users@localhost:22']
env.password = 'password'

name_old = '_old'
name_new = '_new'

def download_last_version():
    print('>>> Update Wordpress...')
    sudo('cd /var/www/wordpress')
    sudo('wget http://wordpress.org/latest.tar.gz')
    sudo('tar xzfv latest.tar.gz')
    sudo('rm latest.tar.gz')  
    print('>>> done...')
    clean_download()

def clean_download():
    print('>>> Clean download...')
    sudo('cd wordpress')
    sudo('mv wp-admin wp-admin%s' % name_new)
    sudo('mv wp-includes wp-includes%s' % name_new)
    sudo('mv wp-admin%s wp-includes%s ..' %(name_new, name_new))  
    sudo('rm -rf wordpress')
    print('>>> done...')
    backup_old_folders()

def backup_old_folders():
    print('>>> Backup...')
    sudo('mv wp-admin wp-admin%s' % name_old)
    sudo('mv wp-includes wp-includes%s' % name_old)
    sudo('mkdir backup')
    sudo('mv wp-admin% wp-includes% backup' %(name_old, name_old))
    sudo('mv wp-admin%s wp-admin' % name_new)
    sudo('mv wp-includes%s wp-include' % name_new)
    print('>>> done...')
    print('>>> Visited http://yourdomain.com/wp-admin/upgrade.php to finish update...')

def deploy():
    download_last_version()











