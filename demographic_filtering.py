import numpy as np
import pandas as pd

d1 = pd.read_csv("d1_nona.csv")


d1 = d1.sort_values("total_events", ascending=False)
output = d1['total_events'].head(20).values.tolist()
  
  