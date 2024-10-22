from damdata_parse.arg_parse import parse_args
from damdata_parse.df_creator import starter_df
from damdata_parse.qc_checker import whole_process as qc_checker


def main():
    # Step 1: Parse the command-line arguments
    args = parse_args()

    # parse the mode to run in
    mode = args.mode

    if mode == 'create_csv':
        input_dir = args.dir
        output = args.output
        starter_df(input_dir, output)

    if mode == 'generate_db':
        samplesheet = args.samplesheet
        if qc_checker(samplesheet):
            print('Passed QC')


    else:
        print("Mode is invalid. Current supported modes are: create_csv")


# Step 5: Call the 'main' function when the script is executed
if __name__ == "__main__":
    main()
