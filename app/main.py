import sys
import os


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        known_commands = ["exit", "echo", "type", "pwd", "cd"]

        # Wait for user input
        paths = os.environ.get('PATH').split(':')
        command = input()
        home_path = os.environ.get('HOME')
        # print(paths)
        args = command.split()

        match args[0]:
            case "exit":
                if args[1] == "0":
                    break
            case "echo":
                sys.stdout.write(" ".join(args[1:]) + "\n")
            case "pwd":
                sys.stdout.write(os.getcwd() + '\n')
            case "cd":
                try:
                    path = args[1]
                    if args[1] == '~':
                        path = home_path
                    os.chdir(path)
                except:
                    sys.stdout.write(f"cd: {args[1]}: No such file or directory\n")
            case "type":
                if args[1] in known_commands:
                    sys.stdout.write(f"{args[1]} is a shell builtin\n")
                else:
                    for path in paths:
                        if os.path.isdir(path) and args[1] in os.listdir(path):
                            sys.stdout.write(f"{args[1]} is {path}/{args[1]}\n")
                            break
                    else:
                        sys.stdout.write(f"{args[1]}: not found\n")
            case '-':
                for path in paths:
                    if os.path.isdir(path) and args[0] in os.listdir(path):
                        os.system(command)
                        break
                else:
                    sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
