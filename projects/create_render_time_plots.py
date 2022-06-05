import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 5, 3, 5, 7, 8]
z = [4, 5, 2, 8, 4, 5]

def get_data_EU06a():
    distances = [100, 200, 300, 400, 500, 600, 700, 800]
    render_durations = {
        "Mesh": [1.31601, 0.749037, 0.639009, 0.608012, 0.60078, 0.59861, 0.599779, 0.603195],
        "VoxelSize=0.1 m": [15.9278, 5.15631, 2.74227, 1.94011, 1.66866, 1.60061, 1.55002, 1.52213],
        "VoxelSize=0.2 m": [10.4343, 3.46261, 1.94111, 1.4179, 1.23918, 1.19578, 1.14642, 1.12755],
        "VoxelSize=0.4 m": [7.4412, 2.56865, 1.48648, 1.12587, 1.00384, 0.957644, 0.930222, 0.922824],
        "VoxelSize=0.8 m": [5.99951, 2.55465, 0.724642, 0.969075, 0.8676, 0.827474, 0.813499, 0.800478],
        "VoxelSize=1.6 m": [4.39172, 2.08938, 1.0122, 0.803366, 0.726858, 0.705414, 0.679117, 0.670922],
        "VoxelSize=3.2 m": [4.05637, 1.48067, 0.965016, 0.753649, 0.682155, 0.655521, 0.6412, 0.634275],
        "VoxelSize=6.4 m": [3.59041, 1.34332, 0.900211, 0.723457, 0.650835, 0.629632, 0.617673, 0.603171]
    }

    return (distances, render_durations)

def get_data_EA01a():
    distances = [100, 200, 300, 400, 500, 600, 700, 800]
    render_durations = {
        "Mesh": [0.759103, 0.63972, 0.625177, 0.634955, 0.638453, 0.643574, 0.653634, 0.658293],
        "VoxelSize=0.1 m": [3.32615, 1.81724, 1.5771, 1.41525, 1.36001, 1.32602, 1.29982, 1.24522],
        "VoxelSize=0.2 m": [2.33618, 1.33796, 1.20131, 1.10058, 1.06082, 1.04384, 1.0331, 0.991338],
        "VoxelSize=0.4 m": [1.81812, 1.09462, 0.990952, 0.926355, 0.908886, 0.890739, 0.867996, 0.847874],
        "VoxelSize=0.8 m": [1.5239, 0.953165, 0.860697, 0.820627, 0.793943, 0.79363, 0.782899, 0.771262],
        "VoxelSize=1.6 m": [1.21191, 0.790445, 0.73817, 0.717132, 0.701859, 0.698066, 0.686814, 0.69179],
        "VoxelSize=3.2 m": [1.13831, 0.754821, 0.705398, 0.682151, 0.669546, 0.667704, 0.675575, 0.66431],
        "VoxelSize=6.4 m": [1.07541, 0.721262, 0.678253, 0.661273, 0.647196, 0.643883, 0.641091, 0.635836]
    }

    return (distances, render_durations)

def create_plot(data, out_path):
    plt.rcParams.update({'font.size': 13})
    for key, value in data[1].items():
        plt.plot(data[0], value, label=key)

    plt.xlabel("Distance from camera [m]")
    plt.ylabel("Render duration [s]")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=500)
    plt.clf()


if __name__ == "__main__":
    create_plot(get_data_EU06a(), "../img/results/render_durations_EU06a.png")
    create_plot(get_data_EA01a(), "../img/results/render_durations_EA01a.png")