for n in range(1,101):
    incoud = str(n).find("7")
    if incoud == 0 or incoud == 1 or n%7==0:
        continue
    print(n)
