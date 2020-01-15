# 7. Tip Calculator
bill = input("Bill total? ")
service = input("Level of service: good, fair, or bad ")
tip = int()
if service == "good":
    tip = int(bill) * 0.20
elif service == "fair":
    tip = int(bill) * 0.15
elif service == "bad":
    tip = int(bill) * 0.1

grand_total = int(tip) + int(bill)
print("Tip is $%.2f. Total due is $%.2f" % (tip, grand_total))
