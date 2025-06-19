my_dict={
    'a':100,
    'b':260,
    'c':450,
    'd':50,
    'e':95
}
def get_value(item):
    return item[1]

top_3=sorted(my_dict.items(),key=get_value,reverse=True)[:3]

for key, value in top_3:
    print(f"{key} : {value}")
