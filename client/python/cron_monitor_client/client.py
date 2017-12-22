# coding = utf-8

import logging
import os
import sys
import etcd

_log = logging.getLogger(__name__)


class CronMointorClien(object):
    def __init__(self, host, name, key):
        self.host = host
        self.name = name
        self.key = key

    def start(self):
        pass

    def finish(self, success, ext):
        pass
