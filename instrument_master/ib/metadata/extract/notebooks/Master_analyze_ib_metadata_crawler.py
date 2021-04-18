# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.0
#   kernelspec:
#     display_name: Python [conda env:venv] *
#     language: python
#     name: conda-env-venv-py
# ---

# %%
import glob
import os

import pandas as pd

import helpers.dbg as dbg

# %%
# !ls ..

# %% [markdown]
# ## Symbols

# %%
if False:
    dir_name = ".."
    files = glob.glob(os.path.join(dir_name, "symbols*.csv"))
    dbg.dassert(len(files), 1)
    file_name = files[0]

file_name = "s3://external-p1/ib/metadata/symbols-2021-04-01-143112738505.csv"
print("file_name=%s" % file_name)
symbols = pd.read_csv(file_name, sep="\t")

print(len(symbols))

symbols.head(3)

# %%
symbols.groupby("product").count()

# %% [markdown]
# ## Exchanges

# %%
if False:
    files = glob.glob(os.path.join(dir_name, "exchanges*.csv"))
    dbg.dassert(len(files), 1)
    file_name = files[0]
file_name = "s3://external-p1/ib/metadata/exchanges-2021-04-01-143112738505.csv"

print("file_name=%s" % file_name)
exchanges = pd.read_csv(file_name, sep="\t")

print(len(exchanges))

exchanges.head(3)

# %% [markdown]
# ## Products

# %%
print(symbols["product"].unique())

# %% [markdown]
# ## Markets

# %%
markets = sorted(symbols["market"].unique())
print("\n".join(markets))

# %%
grouped = symbols.groupby("market")

count = grouped[["product"]].count()
count = count.sort_values(by="product", ascending=False)

count.plot()

print(count.head(10))

# %%
idx = 0
market = count.index[idx]
print("market=", market)
mask = symbols["market"] == market
symbols_tmp = symbols[mask]

grouped = symbols_tmp.groupby("product")

grouped[["product"]].count()

# %%
pd.set_option("display.max_colwidth", 100)

# %%
symbols_tmp[["product", "url"]]

# %%
symbols_tmp["url"].values

# %%