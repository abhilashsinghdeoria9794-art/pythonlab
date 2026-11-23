import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    "Physics": [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    "Chemistry": [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    "English": [80, 84, 72, 91, 76, 80, 70, 95, 77, 89]
}

df = pd.DataFrame(data)
subjects = ["Mathematics", "Physics", "Chemistry", "English"]

melted = df.melt(id_vars="Student", value_vars=subjects, var_name="Subject", value_name="Score")
plt.figure(figsize=(10, 5))
sns.histplot(data=melted, x="Score", hue="Subject", kde=True, bins=6)
plt.title("Subject-Wise Score Distributions")
plt.show()

sns.pairplot(df[subjects], diag_kind="kde")
plt.suptitle("Pairwise Relationships Across Subjects", y=1.02)
plt.show()

plt.figure(figsize=(7, 5))
sns.heatmap(df[subjects].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Subject Correlation Heatmap")
plt.show()