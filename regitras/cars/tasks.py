# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    print 'TASK #1'
    return x + y


@shared_task
def mul(x, y):
    print 'TASK #2'
    return x * y


@shared_task
def xsum(numbers):
    print 'TASK #3'
    return sum(numbers)
