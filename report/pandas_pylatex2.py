import numpy as np
import pylatex as pl
import pandas as pd

df = pd.DataFrame({'a': [1,2,3], 'b': [9,8,7]})
df.index.name = 'x'

M = np.matrix(df.values)

doc = pl.Document()

with doc.create(pl.Section('Matrix')):
    doc.append(pl.Math(data=[pl.Matrix(M)]))

with doc.create(pl.Section('Table')):
    with doc.create(pl.Tabular('ccc')) as table:
        table.add_hline()
        table.add_row([df.index.name] + list(df.columns))
        table.add_hline()
        for row in df.index:
            table.add_row([row] + list(df.loc[row,:]))
        table.add_hline()


# doc.generate_pdf('full', clean_tex=False)
doc.generate_tex('report/tex/full3')