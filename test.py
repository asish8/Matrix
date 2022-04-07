import os
import pandas as pd
import traceback
from datetime import timedelta


def abc():
    # print("Asish")
    List = ["A", "B", "C", "D", "E"]
    # print(List[0])


abc()

c = os.getcwd()
# print("current directory: " , c, type(c))

di = c + "\DG_rnhr_consumption"
# print("changed", di)

df_main = pd.read_csv("_edit.csv")
df_main["runhour"] = "NA"
df_main["fuel"] = "NA"


def search_calculate(id):
    for root, dirs, files in os.walk(di):
        Total_r = "NA"
        Total_f = "NA"
        try:
            if id in files:
                # print("inside",id)
                path_a = os.path.join(root, id)
                # print("jhjpjo", path_a)
                df = pd.read_csv(path_a)
                Total_r = str(timedelta(seconds=int(df['runhour'].sum())))
                Total_f = df['fuel_consumption'].sum()

                # print(Total_r)
        except Exception as e:
            print(e)
            # print(traceback.format_exc())
        # print(Total_f, Total_r)
        return Total_f, Total_r


for i in range(len(df_main)):
    id=df_main["thing_id"].iloc[i]
    # print(id, type(id))
    k = search_calculate(str(id)+".csv")
    
    df_main["runhour"].iloc[i] = k[1]
    df_main["fuel"].iloc[i] = k[0]

df_main.to_csv("df_main.csv")

print(df_main)
