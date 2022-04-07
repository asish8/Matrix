import pandas as pd

def citysearch(city,l):
    status = False
    if city in l:
        status = True   
    return status
       

df = pd.read_csv("things_city.csv")
df["status"]="NA"


fb=pd.read_csv("fuelbuddy cities.csv")
c = list(fb["City"])
print(c, type(c))



for i in range(len(df)):
    status=citysearch(df["City"].iloc[i], c)
    df["status"].iloc[i]=status

df.to_csv("_edit.csv", index=False)