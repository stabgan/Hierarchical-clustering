# Hierarchical Clustering

Customer segmentation using agglomerative hierarchical clustering on mall customer data.

## What It Does

Segments 200 mall customers into 5 distinct groups based on **Annual Income** and **Spending Score** using bottom-up (agglomerative) hierarchical clustering with Ward's linkage method.

### Methodology

1. Load and extract features from `Mall_Customers.csv`
2. Build a **dendrogram** using Ward's minimum variance method to visualize cluster distances and determine optimal `k`
3. Fit **Agglomerative Clustering** with `k=5` and Euclidean distance
4. Visualize the resulting customer segments

Both Python and R implementations follow the same workflow and produce identical results.

## Dataset

`Mall_Customers.csv` — 200 records, 5 columns:

| Column | Description |
|---|---|
| CustomerID | Unique identifier |
| Genre | Gender |
| Age | Customer age |
| Annual Income (k$) | Yearly income in thousands |
| Spending Score (1-100) | Mall-assigned spending score |

Only **Annual Income** and **Spending Score** (columns 4–5) are used for clustering.

## Dependencies

### Python

```bash
pip install numpy matplotlib pandas scipy scikit-learn
```

### R

```r
install.packages("cluster")
```

## How to Run

```bash
# Python
python hc.py

# R
Rscript hc.R
```

Both scripts expect `Mall_Customers.csv` in the working directory. Each produces two plots: a dendrogram and a cluster visualization.

## Tech Stack

- 🐍 Python 3 / R
- 📊 matplotlib / `clusplot`
- 🔬 scikit-learn (`AgglomerativeClustering`)
- 🧮 scipy (`linkage`, `dendrogram`)
- 🐼 pandas / numpy

## Known Issues

- **Hardcoded cluster count:** Both scripts fix `k=5`. No programmatic elbow or silhouette analysis is performed — the dendrogram is provided for visual inspection only.
- **Blocking plots (Python):** `plt.show()` blocks execution. Close each plot window to proceed to the next one.
- **No train/test split:** This is unsupervised clustering — no splitting is needed, but the code has no evaluation metric beyond visual inspection.

## License

MIT — see [LICENSE](LICENSE).
