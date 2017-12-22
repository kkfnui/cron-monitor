# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Task(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    key = models.CharField(max_length=128)

    create_by = models.CharField(max_length=64)
    update_by = models.CharField(max_length=64)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    invalid = models.BooleanField()

    last_status = models.IntegerField()
    last_cost = models.IntegerField()
    last_run = models.DateTimeField()

    cost_threadhold = models.IntegerField()
    idle_interval_threadhold = models.IntegerField()


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    task_id = models.IntegerField()
    task_name = models.CharField(max_length=128)
    start_at = models.DateTimeField()
    stop_at = models.DateTimeField()
    status = models.IntegerField()
    cost = models.IntegerField()
