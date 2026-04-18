import pandas as pd

gdf = pd.read_csv("data/ecoli_amr_genes.csv")
ecolidf = pd.read_csv("data/ecolicipro.csv")

gdf = gdf[gdf["gene"].notna()]
gdf = gdf[gdf["gene"].str.strip() != ""]

# rows are genome_id. columns are gene names and 1 or 0
gdf["present"] = 1
mat = gdf.pivot_table(
    index="genome_id",
    columns="gene",
    values="present",
    aggfunc="max"
).fillna(0).astype(int)

mat = mat.reset_index()
df = mat.merge(
    ecolidf[["genome_id", "resistant_phenotype"]],
    on="genome_id",
    how="inner"
)

# resistant is 1 susceptible is 0
df["label"] = (df["resistant_phenotype"] == "Resistant").astype(int)

df.to_csv("data/matrixx.csv", index=False)
print("done")