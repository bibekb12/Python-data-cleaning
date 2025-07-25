import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
# sn = ["a", "b", "c"]
# myDat = pd.DataFrame(data, index=[sn])
# mySer = pd.Series(data)

# print(myDat)
# print(mySer)

df = pd.DataFrame(data)

# print(df)

print(df.loc[[0, 1, 2]])
