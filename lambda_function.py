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
    response = subprocess.run("python -m awscli " + commands, shell=True, stdout=subprocess.PIPE , stderr=subprocess.PIPE ,encoding="utf-8")
    print(response.stdout)
    print(response.stderr)
    return event
