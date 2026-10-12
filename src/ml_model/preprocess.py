import pandas as pd
import numpy as np
import os

# Resolve paths relative to this file's location, so this works
# regardless of which directory the script is run from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "..", "..", "dataset", "raw", "ServerMachineDataset")

def load_machine_data(machine_id="machine-1-1"):
    train_path = os.path.join(DATASET_DIR, "train", f"{machine_id}.txt")
    test_path = os.path.join(DATASET_DIR, "test", f"{machine_id}.txt")
    label_path = os.path.join(DATASET_DIR, "test_label", f"{machine_id}.txt")

    train = pd.read_csv(train_path, header=None).values
    test = pd.read_csv(test_path, header=None).values
    labels = pd.read_csv(label_path, header=None).values.flatten()

    return train, test, labels

if __name__ == "__main__":
    train, test, labels = load_machine_data()
    print("Train shape:", train.shape)
    print("Test shape:", test.shape)
    print("Labels shape:", labels.shape)
    print("Anomaly count in test:", labels.sum())
