import pandas as pd
import numpy as np


x=pd.Series([2.1,2.2,4.5,2.7,2.3])
median=np.median(x)
threshold=2
outlier=[]
print(median)
for item in x:
    if (item-median)>threshold:
        outlier.append(item)
        
print(outlier)