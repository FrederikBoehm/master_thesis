import matplotlib.pyplot as plt
import numpy as np

covered_pixels = [1, 4, 9, 16]
min_voxel_size = [0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4]




def output_heatmap(data, output_file, format):
    plt.rcParams.update({'font.size': 13})

    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap="magma_r")

    # Show all ticks and label them with the respective list entries
    ax.set_yticks(np.arange(len(covered_pixels)), labels=covered_pixels)
    ax.set_xticks(np.arange(len(min_voxel_size)), labels=min_voxel_size)

    ax.set_xlabel("Minimum voxel size [m]")
    ax.set_ylabel("Covered pixels")

    # # Loop over data dimensions and create text annotations.
    for x in range(len(min_voxel_size)):
        for y in range(len(covered_pixels)):
            text = ax.text(x, y, format(data[y][x]),
                        ha="center", va="center", color="grey")

    fig.tight_layout()
    plt.savefig(output_file, dpi=500)
    plt.clf()

if __name__ == "__main__":
    render_durations = np.array([
        [8722.81, 12184.4, 16249.9, 16337.4],
        [5823.27, 8198.91, 10126.9, 10465.2],
        [4642.43, 5488.97, 6632.95, 6632.95],
        [5004.1, 4548.52, 4663.93, 5033.91],
        [5994.89, 4998.49, 4783.24, 4679.23],
        [6289.99, 6094.03, 5352.92, 4864.56],
        [6285.66, 6252.5, 6201.03, 5792.99]
    ])
    render_durations = render_durations.T
    output_heatmap(render_durations, "../img/results/render_durations.png", lambda v: f"{round(v)} s")

    flip_errors = np.array([
        [0.072899,	0.097151,	0.155666,	0.163013],
        [0.049363,	0.067785,	0.089264,	0.098614],
        [0.037218,	0.048444,	0.059006,	0.072069],
        [0.033212,	0.038192,	0.044895,	0.052216],
        [0.031505,	0.033758,	0.036825,	0.039874],
        [0.03135,	0.031642,	0.032921,	0.034517],
        [0.03135,	0.031359,	0.031521,	0.032148]
    ])
    flip_errors = flip_errors.T
    output_heatmap(flip_errors, "../img/results/flip_errors.png", lambda v: f"{round(v, 3)}")
