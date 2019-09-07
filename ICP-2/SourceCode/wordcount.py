f = open("t.txt","r")
wc = {}
for w in f.read().split(" "):
    if w not in wc:
         wc[w]= 1
    else:
         wc += 1
for a,b in wc.items():
  print(a,b)
