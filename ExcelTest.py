import pandas as pd
import ctypes
# raw_data = {'col0' : [1, 2, 3, 4],
#             'col1' : [10, 20, 30, 40],
#             'col2' : [100, 200, 300, 400]}


col0 = list(0 for i in range(0,6))
col1 = list(0 for i in range(0,6))
col2 = list(0 for i in range(0,6))
for i in range(0,6,1):
    col0[i] = i+1
    col1[i] = (i+1)*20
    col2[i] = (i+1)*50
raw_data = {'col0', 'col1', 'col2'}
raw_data = pd.DataFrame(raw_data)
raw_data.to_excel(excel_writer='sample1.xlsx')