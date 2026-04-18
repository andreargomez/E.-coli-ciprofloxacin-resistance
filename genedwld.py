import requests
import pandas as pd
import os
import time

os.makedirs("data", exist_ok=True)

df = pd.read_csv("data/ecolicipro.csv")
ids = df["genome_id"].unique().tolist()

batch = 100
genes = []

for i in range(0, len(ids), batch):
    grp = ids[i:i+batch]
    idss = ",".join(str(g) for g in grp)
    url = f"https://www.bv-brc.org/api/sp_gene/?in(genome_id,({idss}))&select(genome_id,gene,product,source)&limit(25000)"

    r = requests.get(url, headers={"Accept": "application/json"}, timeout=90)

    raw = r.json()
    genes.extend(raw)

    time.sleep(2)

gdf = pd.DataFrame(genes)
print(f"{len(gdf)} gene records")

gdf.to_csv("data/ecolig.csv", index=False)
print("done")