import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        known_commands = ["exit", "echo", "type"]

        # Wait for user input
        command = input()
        args = command.split()
        if args[0] == "exit":
            if args[1] == "0":
                break
        elif args[0] == "echo":
            sys.stdout.write(" ".join(args[1:]) + "\n")
        elif args[0] == "type":
            if args[1] in known_commands:
                sys.stdout.write(f"{args[1]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{args[1]}: not found\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
