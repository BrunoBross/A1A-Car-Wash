import sys
from typing import Optional
from package.app.App import App
from package.Config import Config
from package.database.Database import Database

def parseInput(argv: list[str]) -> Optional[int]:
    argc = len(sys.argv)
    match argc: 
        case 1:
            return 0
        case 2:
            if argv[1] == Config.MIGRATION_CODE: return 1
        case _:
            exit(1)

def main() -> None:
    argv = sys.argv
    is_migration = parseInput(argv)
    process = Database if is_migration else App
    process.start()

if __name__ == '__main__':
    main()

