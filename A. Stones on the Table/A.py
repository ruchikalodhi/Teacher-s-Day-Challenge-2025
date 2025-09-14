n = input()
inStr = input()

now = inStr[0]
cnt = 0

for i in range(1,len(inStr)):
    char = inStr[i]
    if(char!=now):
        now = char
    else :
        cnt+=1
        
print(cnt)
