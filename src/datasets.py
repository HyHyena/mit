import numpy as np


def arrays():
    names = []
    sequences = []
    with open("../data/miRNA.txt") as file:
        data = file.readlines()
    i = 0

    for line in data:
        if i % 2 == 0:
            names.append(line.replace('\n', '').split(" ")[0])
        else:
            sequences.append(line.replace('\n', ''))
        i += 1

    np_names = np.array(names)
    np_sequences = np.array(sequences)
    return np_names, np_sequences


def csv_into_array():
    with open("../data/MicroRNA_Target_Sites.csv") as file:
        data = file.readlines()

    names = []
    targets = []
    sequences = []

    for line in data:
        names.append(line.split(",")[1])
        targets.append(line.split(",")[3])
        sequences.append(line.split(",")[6])
    np_names = np.array(names)
    np_targets = np.array(targets)
    np_seq = np.array(sequences)
    return np_names, np_targets, np_seq


if __name__ == "__main__":
    csv_names, csv_targets, csv_seq = csv_into_array()
    np_names, np_seq = arrays()
    dick = dict(zip(np_names, np_seq))
    csv = dict(zip(csv_names, csv_targets))
    result = []
    for name, targets in csv.items():
        if name in np_names:
            result.append(dick[name])
        # else:
        #     print(name)

