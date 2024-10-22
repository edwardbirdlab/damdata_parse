import pandas as pd
import os

def starter_df(import_dir, output):
    """

    :param import_dir:
    :param output:
    :return: A CSV of output that contains the start of the samplesheet
    """

    absolute_paths = []
    dtype = []

    dir_contents = os.listdir(import_dir)
    for dir in dir_contents:
        if os.path.isdir(os.path.join(import_dir, dir)):
            sub_files = os.listdir(os.path.join(import_dir, dir))
            if len(sub_files) > 0:
                for file in sub_files:
                    full_path = os.path.abspath(os.path.join(import_dir, dir, file))
                    absolute_paths.append(full_path)
                    dtype.append(dir)
            else:
                print('There were no data file in: {}'.format(os.path.join(import_dir, dir)))
        else:
            print(dir + ' is not a directory: Skipping')

    cond = [None] * len(dtype)

    df = pd.DataFrame()
    df['condition'] = cond
    df['type'] = dtype
    df['path'] = absolute_paths

    df.to_csv(output, index=False)