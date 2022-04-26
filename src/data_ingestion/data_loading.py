from pathlib import Path

import pandas as pd

df = pd.read_csv(Path("C:/Formation/portuguese-bank-marketing-vscode/data/raw/bank-full.csv"), sep=";", header=0, encoding = 'latin-1', low_memory = False)
df

