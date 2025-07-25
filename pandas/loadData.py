import pandas as pd
from dataApi import demo_data

imp = demo_data()

print("api Limit", imp["header"]["X-RateLimit-Remaining"])

if "error" not in imp:
    df = pd.json_normalize(imp["data"])
    # limit_remain = pd.json_normalize(imp.header[])
    print(df)
else:
    print("Error in getting data from the api,", imp["error"])
