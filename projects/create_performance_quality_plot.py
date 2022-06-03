import matplotlib.pyplot as plt

def get_data_PR04a():
    lod_size = [0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4]
    # lod_size = [0, 1, 2, 3, 4, 5, 6]
    data = {
        "FLIP": [0.025766,	0.022173,	0.030333,	0.038439,	0.04428,	0.058313,	0.061157],
        "Time": [171.676, 127.218, 106.393, 92.6528, 86.7085, 66.18, 41.8291]
    }

    return (lod_size, data)

def get_data_EA01a():
    lod_size = [0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4]
    # lod_size = [0, 1, 2, 3, 4, 5, 6]
    data = {
        "FLIP": [0.066111,	0.064404,	0.059674,	0.068491,	0.078282,	0.086487,	0.115491],
        "Time": [685.453, 452.881, 335.395, 279.225, 216.635, 205.047, 194.437]
    }

    return (lod_size, data)

def create_plot(data, out_path):
    plt.rcParams.update({'font.size': 13})
    fig, ax1 = plt.subplots()

    ax1.set_xlabel("Voxel size [m]")
    ax1.set_ylabel("FLIP error")
    flip_plot = ax1.plot(data[0], data[1]["FLIP"], label="FLIP error")

    ax2 = ax1.twinx()

    ax2.set_ylabel("Render duration [s]")
    duration_plot = ax2.plot(data[0], data[1]["Time"], "--", label="Duration")

    plots = flip_plot+duration_plot
    labels = [l.get_label() for l in plots]
    
    plt.legend(plots, labels)
    plt.tight_layout()
    plt.savefig(out_path, dpi=500)
    plt.clf()


if __name__ == "__main__":
    create_plot(get_data_PR04a(), "../img/results/performance_quality_PR04a.png")
    create_plot(get_data_EA01a(), "../img/results/performance_quality_EA01a.png")