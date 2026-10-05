## Plots BB scores over time
## MAT 20260916

import matplotlib.pyplot as plt
import analyzeBoxBlocks as abb
from scatterLinePlot import scatterLinePlot as slp

# hardcoded folder path for now
folder_path = (
    r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Assessments\Post-Op\BoxBlocks"
)

# analyze data
my_data = abb.analyzeBB(folder_path)

# plot data
print(my_data)
slp(
    my_data["DSI"].to_numpy(),
    my_data["Blocks"].to_numpy(),
    title="BB",
    x_label="DSI",
    y_label="Blocks",
    save_path=r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Analysis\BoxAndBlocks",
)
