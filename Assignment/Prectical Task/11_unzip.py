tpl=[(1,'A',True),(4,'B',False),(7,'C',True)]

unziped=list(zip(tpl))

unziped_list=[list(i) for i in unziped]

for i, lst in enumerate(unziped_list,start=1):
    print(f"List {i} : {lst}")



