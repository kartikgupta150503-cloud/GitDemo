"""
Amount = P * (1 + R / 100) ^ T
Compound Interest = Amount - P
"""

principal = float(input("Enter the Principal Amount: " ))
rate = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time duration: "))

amount1 = principal * ((1 + rate / 100) ** time)
amount2 = principal * pow((1 + rate / 100), time)
ci1 = amount1 - principal
ci2 = amount2 - principal

print("The Compound interest is ", ci1)
print("The Compound interest is ", ci2)