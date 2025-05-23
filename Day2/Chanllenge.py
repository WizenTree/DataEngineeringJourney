import pandas as pd

name = input("Enter a Name: ")
score = input("Enter a Score: ")

new_row = pd.DataFrame([[name, score]], columns=["name","score"])

with open (r"E:\VISHAL NAIKAR\DataEngineeringBootCamp\Phase1_CoreSkills\Day1\scores.csv", "a") as file:
    new_row.to_csv(file, header = False, index=False, lineterminator='\n')

print ("Row added succesfully ")
df = pd.read_csv(r"E:\VISHAL NAIKAR\DataEngineeringBootCamp\Phase1_CoreSkills\Day1\scores.csv")
print(df)