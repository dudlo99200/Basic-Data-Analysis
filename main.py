import numpy as np
import matplotlib.pyplot as plt

# Example dataset: Student exam scores (out of 100)
scores = np.array([85, 90, 87, 89, 88, 78, 90, 99, 95, 96])
print("Scores:", scores)

mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev = np.std(scores)

print(f"Mean score: {mean_score}")
print(f"Median score: {median_score}")
print(f"Standard Deviation: {std_dev}")

# Filter students who scored above 90
high_scores = scores[scores>90]
print("High scores(>90):", high_scores)

# plot a histogram of the scores
plt.hist(scores, bins=5, edgecolor='black')
plt.title("Distribution of student scores")
plt.xlabel("Scores")
plt.ylabel("Number of students")
plt.show()

# pass percentage and top 3
pass_percentage = np.mean(scores >= 70) * 100
print(f"Pass percentage: {pass_percentage}%")

top_3_scores = np.sort(scores)[-3:][::-1]
print("Top 3 scores:", top_3_scores)
