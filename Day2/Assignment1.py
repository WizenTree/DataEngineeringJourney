import pandas as pd

df = pd.read_csv(r"E:\VISHAL NAIKAR\DataEngineeringBootCamp\Phase1_CoreSkills\Day1\scores.csv")

df["score"] = df["score"] +5

df["status"] = df["score"].apply(lambda x: "pass" if x>=90 else "fail")

df.to_csv("updated_scores.csv", index=False)

print("Updated pipeline complete!")