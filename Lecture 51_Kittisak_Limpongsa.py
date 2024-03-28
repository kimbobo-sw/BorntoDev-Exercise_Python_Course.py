def Vat(total_Price):
    result = total_Price+(total_Price * 7 /100)
    return result

x = int(input())
print(int(Vat(x)))