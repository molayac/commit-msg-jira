#!/usr/bin/env python

from distutils.core import setup

setup(name='commit-msg-jira',
      version='1.0',
      description='Hook commit-msg to send worklog to JIRA',
      author='Marlon Olaya',
      author_email='molayaa@psl.com.co',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['jiraworklog'],
      install_requires=['jira', 'configparser', 'tzlocal'],
      scripts=['commit-msg']
     )