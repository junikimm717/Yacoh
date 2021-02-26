#!/usr/bin/env python3

import json
import subprocess
import os

os.chdir("yacoh")
print(os.getcwd())

from config import compile_command, run_command

s = json.loads(open("../tests.json", "r").read())
tests = s["tests"]

subprocess.check_call(compile_command)

for test in tests:
    print('_'*20)
    print(f'INPUT:\n{test["input"]}')
    p = subprocess.Popen(run_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    output, stderr = p.communicate(input=bytes(test["input"], 'utf-8'))
    
    output = output.decode().rstrip() if output is not None else ""
    stderr = stderr.decode().rstrip() if stderr is not None else ""
    expected = test["output"].rstrip()

    print(f'OUTPUT:\n{output}\nSTDERR:\n{stderr}\nEXPECTED:\n{expected}')
    if p.returncode != 0:
        print("non-zero exit code.")
        exit(1)
