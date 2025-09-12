n = int(input())
for i in range(n):
  st = input()
  l = len(st)
  if l <= 10:
    print(st)
  else:
    print(st[0], 12, st[1-1], sep="")

