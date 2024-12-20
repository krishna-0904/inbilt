# val="ABctomKJUY"
# print(val.swapcase())

val="ABctomKJUY"
for x in val:
    ord_val=ord(x)
    if x in range(65,91):
        print(chr(ord_val+32),end='')
    elif x in range(97,123):
        print(chr(ord_val-32),end='')
    else:
        print(x,end='')