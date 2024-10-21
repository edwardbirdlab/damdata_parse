from damdata_parse.arg_parse import parse_args


def main():
    # Step 1: Parse the command-line arguments
    args = parse_args()

    # parse the mode to run in
    mode = args.mode

    if mode == 'parse':
        print("Cool mode")

    else:
        print("Mode is invalid. Current supported modes are: prase")


# Step 5: Call the 'main' function when the script is executed
if __name__ == "__main__":
    main()
