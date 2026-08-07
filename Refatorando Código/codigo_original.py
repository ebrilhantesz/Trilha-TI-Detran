n = int(input("quantas notas? "))
l = []
i = 0
while i < n:
    x = float(input("digite a nota: "))
    l.append(x)
    i = i + 1

s = 0
for j in l:
    s = s + j
m = s / n

if m >= 6:
    print("aprovado")
else:
    print("reprovado")
print(m)
