# Hierarchical Clustering

Agglomerative hierarchical clustering on mall customer data, implemented in both Python and R.

## Overview

This project segments customers from a mall dataset into groups based on **Annual Income** and **Spending Score** using agglomerative (bottom-up) hierarchical clustering with Ward's linkage method.

Both implementations follow the same workflow:

1. Load `Mall_Customers.csv` (200 records, 5 fields)
2. Extract the two features: Annual Income and Spending Score
3. Build a dendrogram to visualize cluster distances and determine the optimal number of clusters
4. Fit agglomerative clustering with `k=5` using Ward's method and Euclidean distance
5. Plot the resulting clusters

## Dataset

`Mall_Customers.csv` — 200 rows with columns:

| Column | Description |
|---|---|
| CustomerID | Unique ID |
| Genre | Gender |
| Age | Customer age |
| Annual Income (k$) | Yearly income in thousands |
| Spending Score (1-100) | Mall-assigned spending score |

Only columns 4–5 (Annual Income, Spending Score) are used for clustering.

## Dependencies

### Python (`hc.py`)

- numpy
- matplotlib
- pandas
- scipy
- scikit-learn

```bash
pip install numpy matplotlib pandas scipy scikit-learn
```

### R (`hc.R`)

- `cluster` (for `clusplot`)

```r
install.packages("cluster")
```

## Usage

```bash
# Python
python hc.py

# R
Rscript hc.R
```

Both scripts expect `Mall_Customers.csv` in the working directory. Each produces two plots: a dendrogram and a cluster scatter plot.

## Known Issues

- **`affinity` parameter deprecated (Python):** `AgglomerativeClustering(affinity='euclidean')` was deprecated in scikit-learn 1.2 and removed in 1.4. Modern versions use `metric='euclidean'` instead. The current code will raise a warning or error on scikit-learn ≥ 1.4.
- **`sklearn.cross_validation` removed:** Commented-out imports reference `sklearn.cross_validation`, which was removed in scikit-learn 0.20+. The correct module is `sklearn.model_selection`. This doesn't affect execution since the lines are commented out, but is worth noting.
- **No file missing from the dendrogram GIF:** The original README embedded an external GIF (`dashee87.github.io`). That link may break over time.
- **Hardcoded cluster count:** Both scripts fix `k=5` without programmatic elbow/silhouette analysis. The dendrogram is shown for visual inspection only.

## License

MIT — see [LICENSE](LICENSE).
