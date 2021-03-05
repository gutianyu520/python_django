# coding=UTF-8

import time
from celery import task

# create celery task
@task
def show():
    print('hello...')
    time.sleep(5)
    print('world...')