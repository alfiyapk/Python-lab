a=[8,6,7,4,5]
b=[5,4,3,2,1]
if len(a)==len(b):
    print("a. the list have same length.")
else:
    print("a. the list have different length.")
print(f"b.sum of list1:{sum(a)} & sum of list2: {sum(b)}")
if sum(a)==sum(b):
    print("the list sum to the same value.")
else:
    print("the list sum to not the same value.")
common_values=set(a) & set(b)
if common_values:
    print(f"common values in both lists: {common_values}.")
else:
    print(f"There are no common values in both lists")
