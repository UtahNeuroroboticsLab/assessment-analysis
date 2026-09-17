## Reads all xcel files in given directory, pulls out box and blocks results, and returns as a table
## MAT 20260916

import pathlib
import polars as pl
import datetime as dt
import sys


def analyze_bb(folder_path):

    # init pl dataframe
    my_data = pl.DataFrame()

    # date of implant
    implant_date = dt.date.strptime("20260129", "%Y%m%d")

    # get path incrementer
    pathlist = pathlib.Path(folder_path).glob("**/*.xlsx")

    # increment through folder contents
    for my_path in pathlist:

        # read table
        temp_data = pl.read_excel(my_path)

        # get date from file name
        date_str = str(my_path.name)
        date_str = date_str.split("-")
        date_str = date_str[0]
        date_str = dt.date.strptime(date_str, "%Y%m%d")

        # get days since implant
        dsi = date_str - implant_date
        dsi = dsi.days
        dsi = pl.DataFrame({"DSI": dsi})
        # append to match size of temp_data
        for i in range(len(temp_data) - 1):
            dsi = pl.concat([dsi, dsi], how="vertical")

        # add dsi to temp_data
        temp_data = pl.concat([dsi, temp_data], how="horizontal")

        # concat to output
        my_data = pl.concat([my_data, temp_data], how="vertical")

    # sort data by data
    my_data.sort("DSI")
    return my_data


if __name__ == "main":
    my_path = repr(sys.argv[1])
    my_data = analyze_bb(my_path)
    print(my_data)
