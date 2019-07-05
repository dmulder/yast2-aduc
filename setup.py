#!/usr/bin/env python3
from distutils.core import setup
import os, shutil

if not os.path.exists('build/_scripts'):
    os.makedirs('build/_scripts')
shutil.copyfile('src/clients/aduc.py', 'build/_scripts/aduc')

setup(name='aduc',
    version='1.5',
    description='Active Directory Users and Computers',
    author='David Mulder',
    author_email='dmulder@suse.com',
    url='https://github.com/yast/yast2-aduc',
    scripts=['build/_scripts/aduc'],
    packages=['aduc', 'yast'],
)
