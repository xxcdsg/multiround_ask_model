ss = input()
s = ""
while(ss != "-1") :
    s += ss
    ss = input()
s = s.replace("|","")
s = s.replace(" ","")
print(s)
res = ""
for c in s:
    res += c
    res += ","
res = res.removesuffix(",")
print(res)