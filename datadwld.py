import requests
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

url = "https://www.bv-brc.org/api/genome_amr/?eq(antibiotic,ciprofloxacin)&eq(taxon_id,562)&select(genome_id,genome_name,resistant_phenotype)&limit(20000)"

r = requests.get(
    url,
    headers={"Accept": "application/json"},
    timeout=60
)

data = r.json()
df = pd.DataFrame(data)
print(f"{len(df)} records downloaded")

# keep only phenotypes resistant or susceptible
df = df[df["resistant_phenotype"].isin(["Resistant", "Susceptible"])]
print(f"{len(df)} records after filtering")

df.to_csv("data/ecolicipro.csv", index=False)
print("done")