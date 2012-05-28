#!/bin/bash

export PYTHONPATH=`pwd`:`pwd`/ait_app:`pwd`/lib
export DJANGO_SETTINGS_MODULE="settings.`hostname -s`"
