import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

df = pd.read_csv('certified.csv')

socs = df['SOC_NAME']

socs_set = list(set(socs))
soc_count = pd.DataFrame()
soc_count['SOC_NAME'] = pd.Series(data=socs_set)
c = []
for soc in socs_set:
    c.append(len(df[socs == soc]))

soc_count['COUNT'] = pd.Series(data=c)
soc_count = soc_count.sort_values('COUNT')
print(soc_count)
width = 0.35
index = np.arange(len(soc_count['SOC_NAME']))
plt.bar(index, soc_count['COUNT'], width, color='b')

plt.show()
input()
