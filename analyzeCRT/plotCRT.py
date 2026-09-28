## Plots CRT scores over time
## MAT 20260917

import matplotlib.pyplot as plt
import analyzeCRT as crt

# hardcoded folder path for now
folder_path = (
    r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Assessments\Post-Op\CRT"
)

# analyze data
my_data = crt.analyze_crt(folder_path)

# plot data
print(my_data)
plt.scatter(my_data["DSI"].to_numpy(), my_data["Time"].to_numpy())

plt.xlabel("DSI")
plt.ylabel("Blocks")
plt.title("Blocks")
plt.show()
plt.savefig(
    r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Analysis\BoxAndBlocks\bb.eps",
    format="eps",
)
plt.savefig(
    r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Analysis\BoxAndBlocks\bb.png",
    format="png",
)
