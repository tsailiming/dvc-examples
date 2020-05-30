#!/usr/bin/env python

import dvc.api
import pandas as pd

resource_url = dvc.api.get_url(
    path='data/iris.csv',
    repo='https://github.com/tsailiming/dvc-examples',
    rev='v1.0')

print(resource_url)

df = pd.read_csv(resource_url)
print(df.describe())

