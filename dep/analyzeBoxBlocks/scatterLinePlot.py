# uses matplotlib to scatter plot data the plot a line through the average
# assumes inputs are numpy arrays
# MAT 20260928

import matplotlib.pyplot as plt
import numpy as np


def scatterLinePlot(
    x_data, y_data, title="my_title", x_label="X", y_label="Y", save_path=None
):

    # first scatter plot the data
    plt.scatter(x_data, y_data)

    # init vars
    prev_x = x_data[0]
    reps = 0
    y_sum = 0
    mean_x = np.empty([0, 0])
    mean_y = np.empty([0, 0])

    # append 0 to end of data for recursive mean
    x_data = np.append(x_data, 0)
    y_data = np.append(y_data, 0)

    # then calculate the means for each x value
    # loop over values
    for indx in range(x_data.size):
        # get current x_val
        x_val = x_data[indx]

        # get current y_val
        y_val = y_data[indx]

        # compare current x_val to prev_x
        # if x_val is the same as prev_x, continue accumulating the mean, otherwise finish one mean and start another
        if x_val != prev_x:

            # calculate mean if there multiple reps
            new_y = y_sum / reps

            # append x and y
            mean_x = np.append(mean_x, prev_x)
            mean_y = np.append(mean_y, new_y)

            # set new prev_x
            prev_x = x_val

            # clear reps and y_sum
            y_sum = 0
            reps = 0

        # add y val to y_sum and 1 to reps
        y_sum = y_sum + y_val
        reps = reps + 1

    # plot line with new data
    plt.plot(mean_x, mean_y)

    # add info
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # save if relevant
    if save_path is not None:
        plt.savefig(
            save_path + "\\" + title + ".eps",
            format="eps",
        )
        plt.savefig(
            save_path + "\\" + title + ".png",
            format="png",
        )

    # show plot
    plt.show()
