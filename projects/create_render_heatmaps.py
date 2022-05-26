import matplotlib.pyplot as plt
import numpy as np

covered_pixels = [1, 4, 9, 16]
min_voxel_size = [0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4]




def output_heatmap(data, output_file, format):
    plt.rcParams.update({'font.size': 16})

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
        [341.768, 477.797, 642.012, 640.766],
        [227.731, 322.568, 397.066, 412.077],
        [182.099, 215.277, 260.834, 267.423],
        [203.764, 179.147, 183.69, 198.828],
        [255.162, 202.701, 189.959, 184.693],
        [269.292, 259.237, 219.417, 196.444],
        [268.354, 265.498, 263.707, 242.794]
    ])
    render_durations = render_durations.T
    output_heatmap(render_durations, "../img/results/render_durations.png", lambda v: f"{round(v)}s")

    flip_errors = np.array([
        [0.122832,	0.138516,	0.178828,	0.184992],
        [0.105065,	0.119645,	0.135461,	0.141798],
        [0.094773,	0.104985,	0.113994,	0.123615],
        [0.090468,	0.095632,	0.102074,	0.108101],
        [0.088306,	0.090996,	0.094093,	0.097175],
        [0.088059,	0.088502,	0.090033,	0.091722],
        [0.088059,	0.088073,	0.088357,	0.089215]
    ])
    flip_errors = flip_errors.T
    output_heatmap(flip_errors, "../img/results/flip_errors.png", lambda v: f"{round(v, 3)}")
