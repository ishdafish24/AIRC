import numpy as np
import pandas as pd
import scanpy as sc
import matplotlib.pyplot as plt
from scipy.sparse import issparse

"""
sc.settings.verbosity = 3             # verbosity: errors (0), warnings (1), info (2), hints (3)
sc.logging.print_header()
sc.settings.set_figure_params(dpi=80, facecolor='white')


results_file = 'write/CoreAnalyzedData.h5ad'

adata = sc.read_h5ad('/Users/ishaansareen/CoreData/local.h5ad')
adata.var_names_make_unique()
# adata

num_cells = adata.n_obs
num_genes = adata.n_vars

print("Number of cells:", num_cells)
print("Number of genes:", num_genes)
"""
print("shell test")