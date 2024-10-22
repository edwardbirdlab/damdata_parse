import pandas as pd


def check_extra(df):
    """

    :param df: Input dataframe
    :return: A count of how many reads had a error
    """
    failed_reads = 0
    for val in df.Extras:
        if val != 0:
            failed_reads += 1

    return failed_reads


def check_status(df):
    """

    :param df: Input dataframe
    :return: A count of how many reads had a error
    """
    failed_reads = 0
    for val in df.Status:
        if val != 1:
            failed_reads += 1

    return failed_reads


def import_sheet(path):
    """
    :param path: Input path
    :return: dataframe
    """
    cols = ['Index', 'Date', 'Time', 'Status', 'Extras', 'Monitor_Number', 'Tube_Number', 'Data_Type',
            'NA', 'Light', 'Tube_1', 'Tube_2', 'Tube_3', 'Tube_4', 'Tube_5', 'Tube_6',
            'Tube_7', 'Tube_8', 'Tube_9', 'Tube_10', 'Tube_11', 'Tube_12', 'Tube_13',
            'Tube_14', 'Tube_15', 'Tube_16', 'Tube_17', 'Tube_18', 'Tube_19',
            'Tube_20', 'Tube_21', 'Tube_22', 'Tube_23', 'Tube_24', 'Tube_25',
            'Tube_26', 'Tube_27', 'Tube_28', 'Tube_29', 'Tube_30', 'Tube_31',
            'Tube_32']
    df = pd.read_csv(path, sep='\t', names=cols)

    df['Date'] = pd.to_datetime(df['Date'], format='%d %b %y')
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time
    df.insert(1, 'DateTime', df['Date'].astype(str) + ' ' + df['Time'].astype(str))
    df['DateTime'] = pd.to_datetime(df['DateTime'])

    return df


def get_min_time(df):
    """
    returns the min time
    :param df: dataframe with Datetime col
    :return: Min Datetime
    """

    min_date = df['DateTime'].min()

    return min_date


def get_max_time(df):
    """
    returns the max time
    :param df: dataframe with Datetime col
    :return: Max Datetime
    """

    max_date = df['DateTime'].max()

    return max_date


def check_qc(samplesheet):
    """
    Checks internal DAM QC metics for errors
    :param samplesheet:
    """
    for path in samplesheet['path']:

        sheet = import_sheet(path)

        if check_status(sheet) != 0:
            raise Exception("An error occurred: There are ' + str(check_status(sheet)) + ' errors in sheet: ' + path")
        if check_extra(sheet) != 0:
            raise Exception(
                "An error occurred: There are ' + str(check_extra(sheet)) + ' extra readings in sheet: ' + path")


def check_start_stop(samplesheet):
    """
    Checks start and stop time for each sheet
    :param samplesheet: samplesheet
    """

    # Read the DataFrames into a list
    dataframes = [import_sheet(path) for path in samplesheet['path']]

    # Get min/max datetimes from the DataFrames
    min_dates = [df['DateTime'].min() for df in dataframes]
    max_dates = [df['DateTime'].min() for df in dataframes]

    if len(list(set(min_dates))) != 1:
        raise Exception("An error occurred: There are non uniform start times: " + str(min_dates))
    if len(list(set(max_dates))) != 1:
        raise Exception("An error occurred: There are non uniform stop times: " + str(max_dates))


def whole_process(samplesheet):
    """
    Check inputs files for errors or obvious discrpencies
    :param samplesheet: samplesheet from create_csv
    :return: True if passes checks
    """

    samplesheet_df = pd.read_csv(samplesheet)

    check_qc(samplesheet_df)
    check_start_stop(samplesheet_df)

    return True