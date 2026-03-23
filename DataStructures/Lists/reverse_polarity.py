naimenshe = 0
naibilshe = 100

while True:
    chislo = (naimenshe + naibilshe) // 2
    print(chislo, flush=True)

    widpovidy = input().strip()

    if widpovidy == "=":
        break
    elif widpovidy == "-":
        naibilshe = chislo - 1
    elif widpovidy == "+":
        naimenshe = chislo + 1