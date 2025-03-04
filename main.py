import argparse
from src import clean, check, create


def main():
    parser = argparse.ArgumentParser(
        description="Codebase Analysis Tool - Clean, Check, and Create"
    )
    parser.add_argument(
        "action",
        choices=["clean", "check", "create"],
        help="Select an action to perform",
    )
    args = parser.parse_args()

    if args.action == "clean":
        clean.run()
    elif args.action == "check":
        check.run()
    elif args.action == "create":
        create.run()


if __name__ == "__main__":
    main()
