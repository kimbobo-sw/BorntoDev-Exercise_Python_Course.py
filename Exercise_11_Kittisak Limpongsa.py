n = int(input("กรุณาใส่จำนวนที่ต้องการ: "))

for i in range(1, n + 1):
    # พิมพ์ช่องว่างหน้าบรรทัด
    print(" " * (n - i), end="")
    
    # พิมพ์ดาว
    print("*" * (2 * i - 1))
