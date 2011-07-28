#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8

import os, glob
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Import ODK forms and instances."

    def handle(self, *args, **kwargs):
        path = args[0]
        call_command('import_forms', os.path.join(path, "forms"))
        call_command('import_instances', os.path.join(path, "instances"))
