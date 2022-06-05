import matplotlib.pyplot as plt

def get_data_EU06a():
    lod_size = [0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4]
    # lod_size = [0, 1, 2, 3, 4, 5, 6]
    data = {
        "FLIP": [0.120613,	0.132097,	0.143788,	0.166911,	0.187352,	0.21868,	0.267729],
        "Time": [805.019, 522.369, 376.157, 304.377, 217.929, 200.664, 178.852]
    }

    return (lod_size, data)

def get_data_EA01a():
    lod_size = [0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4]
    # lod_size = [0, 1, 2, 3, 4, 5, 6]
    data = {
        "FLIP": [0.169702,	0.177271,	0.187487,	0.208363,	0.237443,	0.280424,	0.33784],
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
    create_plot(get_data_EU06a(), "../img/results/performance_quality_EU06a.png")
    create_plot(get_data_EA01a(), "../img/results/performance_quality_EA01a.png")