import matplotlib.pyplot as plt
import csv

def plot5(filename, savename, x_label, y_label, y_lim = ()):

    with open(filename) as f:
        reader = csv.reader(f)
        _lines = list(reader)

        lines = []
        tags = []
        for _line in _lines:
            tags.append(_line[0])
            lines.append(list(map(float, _line[1:])))

    plt.clf()
    l1, = plt.plot(lines[0], lines[1], 'o-', linewidth=3, markersize=10)
    l2, = plt.plot(lines[0], lines[2], 'v-', linewidth=3, markersize=10)
    l3, = plt.plot(lines[0], lines[3], 's-', linewidth=3, markersize=10)
    l4, = plt.plot(lines[0], lines[4], 'D-', linewidth=3, markersize=10)
    l5, = plt.plot(lines[0], lines[5], '*-', linewidth=3, markersize=10)
    if y_lim:
        plt.ylim(y_lim)

    font1 = {'weight': 'normal', 'size': 14}
    font2 = {'weight': 'normal', 'size': 12}

    plt.xlabel(x_label, font1)
    plt.ylabel(y_label, font1)

    plt.legend(handles=[l1, l2, l3, l4, l5],
               labels=tags[1:],
               loc='best',
               prop=font2)

    plt.grid()
    plt.tight_layout()
    plt.savefig(savename)
    plt.show()


def plot4(filename, savename, x_label, y_label, y_lim = ()):

    with open(filename) as f:
        reader = csv.reader(f)
        _lines = list(reader)

        lines = []
        tags = []
        for _line in _lines:
            tags.append(_line[0])
            lines.append(list(map(float, _line[1:])))

    plt.clf()
    l1, = plt.plot(lines[0], lines[1], 'o-', linewidth=3, markersize=10)
    l2, = plt.plot(lines[0], lines[2], 'v-', linewidth=3, markersize=10)
    l3, = plt.plot(lines[0], lines[3], 's-', linewidth=3, markersize=10)
    l4, = plt.plot(lines[0], lines[4], 'D-', linewidth=3, markersize=10)
    if y_lim:
        plt.ylim(y_lim)

    font1 = {'weight': 'normal', 'size': 14}
    font2 = {'weight': 'normal', 'size': 12}

    plt.xlabel(x_label, font1)
    plt.ylabel(y_label, font1)

    plt.legend(handles=[l1, l2, l3, l4],
               labels=tags[1:],
               loc='best',
               prop=font2)

    plt.grid()
    plt.tight_layout()
    plt.savefig(savename)
    plt.show()


plot5('BS-Throughput.csv', 'BS-Throughput.pdf', 'Buffer Size (KB)', 'Throughput (Kbps)')
plot5('BS-LossRate.csv', 'BS-LossRate.pdf', 'Buffer Size (KB)', 'Packet Loss Rate (%)', y_lim=(0, 0.1))
plot4('Multi-flow Results.csv', 'Multi-flow Results.pdf', 'Number of Flows', 'Packet Loss Rate (%)')
plot5('random loss.csv', 'random loss.pdf', 'Packet Loss Rate (%)', 'Throughput (Kbps)')
plot4('friendliness_data.csv', 'friendliness_data.pdf', 'Number of Cubic Flows', 'Throughput Ratio')
