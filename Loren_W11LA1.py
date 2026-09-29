MachineLearning = [
    ("Supervised", "Decision Tree"),
    ("Supervised", "Random Forest"),
    ("Unsupervised", "K-Means"),
    ("Unsupervised", "Gaussian Mixture Model")
]

print("Learning Type:", MachineLearning[3][0])

for item in MachineLearning:
    if item[0] == "Supervised":
        print("Supervised : ",  item[1])
    else:
        print("Unsupervised : ", item[1])

