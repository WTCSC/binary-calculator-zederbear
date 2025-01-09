import math
allowed = set("0"+"1")
# binary to decimal
def btd(b):
    d = 0 # decimal num
    for i, v in enumerate(b):
        d += int(v)*(2**(len(b)-i-1))
    return d

# decimal to binary
def dtb(d):
    b = ""
    for i in range(8):
        if d - (2**(8-i-1)) < 0:
            b += "0"
        else:
            b += "1"
            d-=(2**(8-i-1))
    return b

def binary_calculator(bin1, bin2, operator):
    if set(bin2) == set("0"):
        return "NaN"
    if set(bin1) <= allowed and set(bin2) <= allowed:
        pass
    else:
        return "Error"
    dec1 = btd(bin1)
    dec2 = btd(bin2)
    dec_ans = math.floor(eval(str(dec1) + operator + str(dec2)))
    if dec_ans > 255 or dec_ans < 0:
        return "Overflow"
    return dtb(dec_ans)
