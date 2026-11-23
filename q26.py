import matplotlib.pyplot as plt

students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
study_hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]
exam_scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(study_hours, bins=5, color="skyblue", edgecolor="black", alpha=0.8, label="Study Hours")
plt.hist(exam_scores, bins=5, color="orange", edgecolor="black", alpha=0.5, label="Exam Scores")
plt.title("Distribution of Study Hours and Exam Scores")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(study_hours, exam_scores, color="purple", s=70)
for i, s in enumerate(students):
    plt.annotate(s, (study_hours[i], exam_scores[i]), textcoords="offset points", xytext=(0, 6), ha="center")
plt.title("Study Hours vs Examination Score")
plt.xlabel("Study Hours/Week")
plt.ylabel("Exam Score")
plt.grid(True)

plt.tight_layout()
plt.show()