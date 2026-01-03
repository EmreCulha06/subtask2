n = 0        
s = 0         
m = None      
x = int(input("Enter a number (-1 to stop): "))
while x != -1:
    n += 1
    s += x
    if n == 1:
        m = x
    elif x < m:
        m = x
    x = int(input("Enter a number (-1 to stop): "))
if n == 0:
    m = -1
    a = -1
else:
    a = s / n
print("Count (n):", n)
print("Sum (s):", s)
print("Minimum (m):", m)
print("Mean (a):", a)