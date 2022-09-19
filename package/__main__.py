import sys
from typing import Type
from package.Process import Process
from package.app.App import App
from package.Config import Config
from package.app.exception.InvalidArgumentException import InvalidArgumentException
from package.database.Database import Database

COMMAND_LINE_OPTION_MAP = {
    Config.OPTION_APP: App,
    Config.OPTION_DATABASE: Database
}

def parseInput(argv: list[str]) -> Type[Process]:
    argc = len(sys.argv)
    if argc != 2 or argv[1] not in Config.OPTIONS:
        raise InvalidArgumentException

    return COMMAND_LINE_OPTION_MAP[argv[1]]

def main() -> None:
    argv = sys.argv
    process = parseInput(argv)
    process.start()

if __name__ == '__main__':
    main()

