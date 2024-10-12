#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2024 Angel Eckardt
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def ensure_installed(name: str):
    """If the module with the given name is not installed, installs it using `pip install`."""
    try:
        __import__(name)
    except ImportError:
        import pip
        print(f"Module '{name}' not found. Attempting pip install...")
        pip.main(['install', name])

ensure_installed('click')

import click
import os
import subprocess

SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]
TASK = "Publish to GitHub"
REMOTE_URL = "https://github.com/aeckar/usf-cse-resources"

@click.command()
@click.argument('message', required = False)
def publish(message):
    """Adds all changes, commits them with the given message, and pushes them to main."""
    try:
        subprocess.run(['git', 'add', '.'])
        while not message:
            message = click.prompt(f"Enter commit message")
            if not message.strip():
                click.secho(f"Commit message cannot be empty.", fg = 'red')
                message = None
        subprocess.run(['git', 'commit', '--message', f"[{SCRIPT_NAME}] {message}"])
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output = True, text = True)
        click.secho(f"{TASK} succeeded: {REMOTE_URL}", fg = 'green')
    except subprocess.CalledProcessError as e:
        click.secho(f"{TASK} failed with error code: {e.returncode}", fg = 'red')
        click.secho(f"{e.stderr}", fg = 'red')

if __name__ == '__main__':
    publish()