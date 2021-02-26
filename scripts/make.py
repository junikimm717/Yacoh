#!/usr/bin/env python3

# This script DOES NOT PARSE INPUT. It only creates new problems.

import os
import shutil

class Problem:

    def __init__(self, name, template):
        self.name = name
        self.path = os.path.join(os.getcwd(), name)
        if name in os.listdir():
            print(name, "already found.")
            exit(1)

    def make_template(self):
        shutil.copytree(template, name)
        os.chdir(self.path)

class ProblemMaker:

    def __init__(self, template, *names):
        self.problems = [Problem(name, template) for name in names]
        
    def create(self):
        for problem in self.problems:
            problem.make_template()
