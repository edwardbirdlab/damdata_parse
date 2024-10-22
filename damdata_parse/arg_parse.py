import argparse  # Importing argparse to handle command-line arguments

def parse_args():
    # Create a parser object and provide a description of the tool's purpose
    parser = argparse.ArgumentParser(description='A tool for analyzing bulk DAM Data')

    # Required arguments
    parser.add_argument('-m', '--mode', required=True, type=str, help='mode to run: choices = [ parse]')

    # Optional basd on mode
    parser.add_argument('-c', '--csv', type=str, help='Path to input csv')
    parser.add_argument('-d', '--dir', type=str, help='Path to input directory')
    parser.add_argument('-o', '--output', type=str, help='output filename')
    parser.add_argument('-s', '--samplesheet', type=str, help='samplesheet input')


    # Optional args

    return parser.parse_args()
