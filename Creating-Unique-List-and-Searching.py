n = int(input())
a = []
if n >= 0:
    for i in range(n):
       reg =  input()
       if reg not in a:
          a.append(reg)
    s = input()
    print(a)
    if s in a:
        print("Found")
    else:
        print("Not found")