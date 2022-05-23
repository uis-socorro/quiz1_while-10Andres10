print("__________________________")
print("_________ CAPITAL ________")
print("__________________________")

c1 = int(input(" Digite el valor de c1: "))
c2 = int(input(" Digite el valor de c2: "))
c3 = int(input(" Digite el valor de c3: "))
m = 0
Capital_Total = c1 + c2
c1 = c1 + 0.03*c1
c2 = c2 + 0.04*c2

while Capital_Total >= c3:
    m = m + 1
    print("En " + str(m) + "meses pueden hacer el negocio que desean")