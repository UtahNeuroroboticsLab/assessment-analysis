## Reads all excel files in a given directory, parses for CRT results and returns a dataframe of the data
## 20260917 MAT

import polars as pl
import datetime as dt
import pathlib
import sys


def analyzeCRT(folder_path):

    # init pl dataframe
    my_data = pl.Dataframe()

    # implant date
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

        # get days since implant(dsi)
        dsi = date_str - implant_date
        dsi = dsi.days
        dsi = pl.DataFrame({"DSI": dsi})

        # add dsi to temp_data
        temp_data = pl.concat([temp_data, dsi], how="horizontal")

        # add data to main
        my_data = pl.concat([my_data, temp_data], how="vertical")

    # sort data by dsi
    my_data.sort("DSI")
    return my_data


if __name__ == "main":
    my_path = repr(sys.argv[1])
    my_data = analyzeCRT(my_path)
    print(my_data)
