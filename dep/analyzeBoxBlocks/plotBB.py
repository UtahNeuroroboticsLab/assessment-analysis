## Plots BB scores over time
## MAT 20260916

import matplotlib.pyplot as plt
import dep.analyzeBoxBlocks.analyzeBoxBlocks as abb
from mains.scatterLinePlot import scatterLinePlot as slp

# hardcoded folder path for now
folder_path = (
    r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Assessments\Post-Op\BoxBlocks"
)

# analyze data
my_data = abb.analyze_bb(folder_path)

# plot data
print(my_data)
slp(
    up_data["DSI"].to_numpy(),
    up_data["Blocks"].to_numpy(),
    title="BB",
    x_label="DSI",
    y_label="Blocks",
    save_path=r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Analysis\BoxAndBlocks",
)
