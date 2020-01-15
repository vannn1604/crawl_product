# import json

# with open("review.json") as f:
#     data_review = json.load(f)
#     for data in data_review:
#         for d in data["reviews"]:
#             print(d, "------------------------------------------------------")

ab = [3, 4, 5, 6, 7, 8]

for i in range(6):
    for j in range(i + 1, 9):
        print(j)
    print("----------------------------")

