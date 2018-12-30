# -*- coding: utf-8 -*-
"""
:mod:`mahler.scheduler.local.resources -- TODO
==============================================

.. module:: resources
    :platform: Unix
    :synopsis: TODO

TODO: Write long description

"""
import getpass
import subprocess

import psutil

from mahler.core.resources import Resources


CPU_COUNT = psutil.cpu_count()


class LocalResources(Resources):
    def __init__(self, processes=CPU_COUNT):
        self.processes = processes

    def available(self):
        out = subprocess.check_output(['ps', '-u', getpass.getuser(), '-o', 'cmd'])
        n_processes = 0
        for line in str(out, encoding='utf-8').split("\n"):
            n_processes += int("mahler execute" in line)

        return max(self.processes - n_processes, 0)

    def submit(self, tasks, tags, **kwargs):
        command = 'mahler execute'
        if tags:
            command += " --tags " + " ".join(tags)

        for task in tasks:
            if self.available():
                print('Executing command:')
                print(command)
                subprocess.Popen(command.split(" "))
