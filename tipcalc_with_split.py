# 8. Tip Calculator 2 with amount per person
bill = input("Bill total? ")
service = input("Level of service: good, fair, or bad ")
num_of_ppl = input("Split how many ways? ")
tip = int()
if service == "good":
    tip = int(bill) * 0.20
elif service == "fair":
    tip = int(bill) * 0.15
elif service == "bad":
    tip = int(bill) * 0.1

grand_total = int(tip) + int(bill)
total_per_person = int(grand_total) / int(num_of_ppl)
print("Tip is %.2f. Total due is %.2f. Amount per person: %.2f" %
      (tip, grand_total, total_per_person))
