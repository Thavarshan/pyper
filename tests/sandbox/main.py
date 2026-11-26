nums = [1, 2, 2, 1, 67, 67, 67, 8, 9, 0, 0, 3, 4, 5, 5, 5, 5, 6, 2, 1, 5]

# Should print: 1-3, 2-3, 3-1, 4-1...

results = {}

for num in nums:
    if results.get(num) is None:
        results[num] = 1
    else:
        results[num] += 1

for num,  occurence in results.items():
    print(f"{num}-{occurence}")
