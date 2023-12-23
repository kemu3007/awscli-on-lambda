import json
import os

import dotenv
from awscli.clidriver import create_clidriver

dotenv.load_dotenv()


def lambda_handler(event, context):
    print(json.dumps(event))
    commands_path = os.environ.get("COMMANDS_PATH").split(".")
    commands = event
    for path in commands_path:
        commands = commands[path]
    print(commands)
    driver = create_clidriver()
    driver.main(commands.split())
    return event
