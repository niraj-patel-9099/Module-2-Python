dct={'maruti':3,'kia':5,'BMW':2,'GT':1}

asc_dct=dict(sorted(dct.items(), key=lambda item:item[1]))
dsc_dct=dict(sorted(dct.items(), key=lambda item:item[1], reverse=True))
print("Original dictionary: ", dct)
print("sorted in ascending order by value: ",asc_dct)
print("sorted in dscending order by value: ",dsc_dct)