lst_tpl=[(1,2,3),(4,5,6),(7,8,9)]
dct= {tuple(i) for i in lst_tpl}

for i, tpl in enumerate(dct):
    print(f"{i} : {tpl}")