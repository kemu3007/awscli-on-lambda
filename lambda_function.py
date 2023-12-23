import json
import os
import subprocess

import dotenv

dotenv.load_dotenv()


def lambda_handler(event, context):
    print(json.dumps(event))
    commands_path = os.environ.get("COMMANDS_PATH").split(".")
    commands = event
    for path in commands_path:
        commands = commands[path]
    subprocess.run("python -m awscli " + commands, shell=True)
    return event
