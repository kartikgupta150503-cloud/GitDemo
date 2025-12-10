"""
Simple interest = (P * R * T) / 100

Here
P = Principal amount
R = Rate of interest
T = Time duration

"""

principal = float(input("Enter the Principal Amount: " ))
rate = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time duration: "))

si = (principal * rate * time) / 100

print("Simple interest is ", si)