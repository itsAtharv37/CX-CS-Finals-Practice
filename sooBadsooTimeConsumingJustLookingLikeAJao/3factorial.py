# 3. write a Python code to take the input of a number n and then find and display its factorial (n!). For example, 5! = 5x4x3x2x1 i.e., 120.

thou_factorial = int(input('pass em number to which i shall take thou factorial'))
factorial = 1

if thou_factorial < 0:
    print("i shall be banish from thou place")
elif thou_factorial == 0:
    print("ek hai bhai, ek hai - 1")
if thou_factorial > 0:
# else:
    for i in range(1,thou_factorial+1):
        factorial = factorial * i

print(f"factorial be {factorial}")