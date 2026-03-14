# Hierarchical Clustering
# Customer segmentation using agglomerative hierarchical clustering

import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering


def main():
    # Resolve dataset path relative to this script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "Mall_Customers.csv")

    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"Dataset not found: {csv_path}")

    # Load dataset and extract features (Annual Income, Spending Score)
    dataset = pd.read_csv(csv_path)
    X = dataset.iloc[:, [3, 4]].values

    # Build dendrogram to visualize optimal number of clusters
    sch.dendrogram(sch.linkage(X, method="ward"))
    plt.title("Dendrogram")
    plt.xlabel("Customers")
    plt.ylabel("Euclidean distances")
    plt.tight_layout()
    plt.show()

    # Fit Agglomerative Clustering (k=5, Ward linkage, Euclidean distance)
    hc = AgglomerativeClustering(n_clusters=5, metric="euclidean", linkage="ward")
    y_hc = hc.fit_predict(X)

    # Visualize the five customer segments
    cluster_config = [
        ("red", "Cluster 1"),
        ("blue", "Cluster 2"),
        ("green", "Cluster 3"),
        ("cyan", "Cluster 4"),
        ("magenta", "Cluster 5"),
    ]
    for idx, (color, label) in enumerate(cluster_config):
        plt.scatter(X[y_hc == idx, 0], X[y_hc == idx, 1], s=100, c=color, label=label)

    plt.title("Clusters of customers")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
