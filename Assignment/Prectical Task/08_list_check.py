lst_=[1,2,3,[4,5,6]]

for i in lst_:
    if isinstance(i, list):
        print(f"{lst_} contains sub-list {i}")
        break
else:
        print(f"{lst_}doesn't contains sub-list")
