## Plots BB scores over time
## MAT 20260916

import matplotlib.pyplot as plt
import analyzeBoxBlocks as abb

# hardcoded folder path for now
folder_path = (
    r"C:\Users\Marshall\Box\Implant Trial\Data\p202601\Assessments\Post-Op\BoxBlocks"
)

# analyze data
my_data = abb.analyze_bb(folder_path)

# plot data
print(my_data)
plt.scatter(my_data["DSI"].to_numpy(), my_data["Blocks"].to_numpy())

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
