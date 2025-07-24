import matplotlib.pyplot as plt
import seaborn as sns
from load import df

#increase plot size and style
sns.set_style("whitegrid")

#Plot the doctor by state
doctors_sorted = df.sort_values("Doctors",ascending=False)

plt.figure(figsize=(12,6))
sns.barplot(data=doctors_sorted, x="Doctors", y ="State/UT", palette="Blues_d",legend=False)
plt.title("Numbers of doctors by State/UT")
plt.xlabel("Numbers of doctors")
plt.ylabel("State/UT")
plt.tight_layout()
plt.show()


#plot the nursing staff by the state

nurses_sorted = df.sort_values("NursingStaff", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=nurses_sorted, x="NursingStaff", y="State/UT", palette="Greens_d", legend=False)
plt.title("Number of Nursing Staff by State/UT")
plt.xlabel("Number of Nursing Staff")
plt.ylabel("State/UT")
plt.tight_layout()
plt.show()

#top 3 states by numbers of doctors
top_doctors = df[['State/UT','Doctors']].sort_values(by='Doctors',ascending=False).head(3)

#top 3 states by nurses
top_nurses = df[['State/UT','NursingStaff']].sort_values(by='NursingStaff',ascending=False).head(3)

print("Top 3 states by the doctor")
print(top_doctors)

print("Top 3 states by the nurses")
print(top_nurses)
