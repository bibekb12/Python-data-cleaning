import pandas as pd

# mydataset = {
#     'cars': ["BMW","Volvo","Ford","Ferrari"],
#     'passing' : [44,21,36,77]
# }

# myvars = pd.DataFrame(mydataset)

# print (myvars.iloc[[1,2]])
# print(pd.__version__)

# a = [1,7,2]
# myser = pd.Series(a, index = ["one","two","three"])
# print(myser["three"])

calories = {"day1": 420, "day2": 380, "day3": 400}

myvar = pd.Series(calories, index=["day1", "day2"])

print(myvar)
