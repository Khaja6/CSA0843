s=str(input("s:"))
t=str(input("t:"))
g=[]
h=[]
for i in s :
	if i not in g:
		g.append(s.index(i))
for k in t:
	if k not in h:		
		h.append(t.index(k))	
if g ==h:
	print("true")
else:
	print("false")
