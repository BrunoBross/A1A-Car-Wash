import sys
from typing import Dict, Type
from package.Process import Process
from package.app.App import App
from package.Config import Config
from package.app.exception.InvalidArgumentException import InvalidArgumentException
from package.database.Database import Database

COMMAND_LINE_OPTION_MAP: Dict[Config.CommandLineArgument, Type[Process]] = {
    Config.CommandLineArgument.APP: App,
    Config.CommandLineArgument.DATABASE: Database,
}


def parseInput(argv: list[str]) -> Type[Process]:
    argc = len(sys.argv)
    if argc != 2 or not Config.CommandLineArgument(argv[1]):
        raise InvalidArgumentException

    return COMMAND_LINE_OPTION_MAP[Config.CommandLineArgument(argv[1])]


def main() -> None:
    argv = sys.argv
    process = parseInput(argv)
    process.start()


if __name__ == "__main__":
    main()
