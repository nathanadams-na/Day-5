scores = input("Input a list of scores:\t").split()
current_score = 0
last_biggest = 0
for score in scores:
    current_score = int(score)
    if current_score > last_biggest:
        last_biggest = current_score
print(f"The largest score is: {last_biggest}")
