from os         import path
from click      import *
from subprocess import run
from subprocess import CalledProcessError

SCRIPT_NAME = path.splitext(path.basename(__file__))[0]
TASK = "Publish to GitHub"
REMOTE_URL = "https://github.com/aeckar/usf-cse-resources"

@command()
@argument('message', required = False)
def publish(message):
    """Adds all changes, commits them with the given message, and pushes them to main."""

    try:
        run(['git', 'add', '.'])
        while not message:
            message = prompt(f"Enter commit message")
            if not message.strip():
                secho(f"Commit message cannot be empty.", fg = 'red')
                message = None
        run(['git', 'commit', '--message', f"[{SCRIPT_NAME}] {message}"])
        run(['git', 'push', '-u', 'origin', 'main'], capture_output = True, text = True)
        secho(f"{TASK} succeeded: {REMOTE_URL}", fg = 'green')
    except CalledProcessError as e:
        secho(f"{TASK} failed with error code: {e.returncode}", fg = 'red')
        secho(f"{e.stderr}", fg = 'red')

if __name__ == '__main__':
    publish()