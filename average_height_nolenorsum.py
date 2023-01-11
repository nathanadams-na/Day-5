heights = input("Input a list of heights seperated by commas:\t").split(',')
total = 0
num_samples = 0
for height in heights:
    total += int(height)
    num_samples += 1
average = total / num_samples
print(total)
print(num_samples)
print(f"Average height is: {average}")