## Plots CRT scores over time
## MAT 20260917

import matplotlib.pyplot as plt
import analyzeCRT as crt
from scatterLinePlot import scatterLinePlot as slp
import polars as pl

# hardcoded folder path for now
folder_path = (
    r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Assessments\Post-Op\CRT"
)

# analyze data
my_data = crt.analyzeCRT(folder_path)

# split into ups and downs
up_data = my_data.filter(pl.col("Case") == "up")
down_data = my_data.filter(pl.col("Case") == "down")

# plot up data
print(my_data)
slp(
    up_data["DSI"].to_numpy(),
    up_data["Time"].to_numpy(),
    title="CRT UP",
    x_label="DSI",
    y_label="Transfer Time (s)",
    save_path=r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Analysis\CRT",
)

slp(
    down_data["DSI"].to_numpy(),
    down_data["Time"].to_numpy(),
    title="CRT Down",
    x_label="DSI",
    y_label="Transfer Time (s)",
    save_path=r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Analysis\CRT",
)
