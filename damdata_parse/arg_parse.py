import argparse  # Importing argparse to handle command-line arguments

def parse_args():
    # Create a parser object and provide a description of the tool's purpose
    parser = argparse.ArgumentParser(description='A tool for analyzing bulk DAM Data')

    # Required arguments
    parser.add_argument('-m', '--mode', required=True, type=str, help='mode to run: choices = [ parse]')

    # Optional basd on mode
    parser.add_argument('-c', '--csv', type=str, help='Path to input csv')


    # Optional args

    return parser.parse_args()
