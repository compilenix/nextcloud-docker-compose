#!/usr/bin/env python3

import os
import subprocess

os.chdir('./instances')

first = True
for instance in os.listdir('./'):
    if not os.path.isdir(instance):
        continue
    if 'new_instance_template' in str(instance):
        continue

    print(f'update instance: {instance}')
    os.chdir(instance)

    if first:
        first = False
        subprocess.call('docker-compose pull'.split(' '))

    subprocess.call(f'docker-compose down'.split(' '))
    subprocess.call(f'docker-compose up -d'.split(' '))
    os.chdir('..')

os.chdir('..')
