ma,rev = input().split()
ma,rev = int(ma), int(rev)
Lit1 = [ int(x) for x in input().split()]
for i in range(0,rev) :
    vt1,ft1 = input().split()
    vt1,ft1 = int(vt1), int(ft1)
for i in range(0,rev):
    print(min(Lit1[vt1-1:ft1]))
