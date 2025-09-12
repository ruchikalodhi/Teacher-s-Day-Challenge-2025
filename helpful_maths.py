# 339A - Helpful Maths

s = input()
arr = [x for x in s if x.isdigit()]
ans = '+'.join(sorted(arr))
print(ans)