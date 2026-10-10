import pandas as pd
import numpy as np


df = pd.read_csv("adult.csv", sep= ';')
df = df.replace({"?": np.nan})
df = df.drop(columns=["race"])
df = df.fillna("--No Data--")

# Proportion of people who earn more than $50k:
salary_more_than_50k =df[df["income"] == ">50K"]
a = (salary_more_than_50k["income"].count())
b = (df["income"].count())

proportion = (a/b)*100
print(f"{round(proportion,2)}%")



# Average age of people who earn more than $50k:
average_age = salary_more_than_50k["age"].mean()
response = (f"{round(average_age,1)} years old")
# print(response)


# Average age by education:


average_age_by_edu = (df.groupby("education")["age"].mean())
# print(round(average_age_by_edu,1))


# Proportion of men and women who earn more than $50k:

male = (salary_more_than_50k['sex'] == "Male").sum()
female = (salary_more_than_50k['sex'] == "Female").sum()
all_male =(df['sex'] == 'Male').sum()
all_female =(df['sex'] == 'Female').sum()
proportion2 = (male /all_male)*100
proportion3 = (female /all_female)*100

#print(f"{round(proportion2,3)}% of all men earn more than $50k")
#print(f"{round(proportion3,3)}% of all women earn more than $50k")

# Median hours worked per week for people who earn more than $50k:
median = (salary_more_than_50k["hours.per.week"]).median()

#print(median)
