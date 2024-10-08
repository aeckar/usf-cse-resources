def ensure_installed(name: str):
    """If the module with the given name is not installed, installs it using `pip install`."""
    try:
        __import__(name)
    except ImportError:
        import pip
        print(f"Module '{name}' not found. Attempting pip install...")
        pip.main(['install', name])

ensure_installed("click")

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