import json,os,sys,urllib.request as w
A=[0,100,320,330,500,900,0,100,320,330,500,900,0]
P0=['dddd\x96\x96\x96\x96nnx\x82iin}dddxi_ZdinnPdddd','2<FF<PddFdnsFisxFdsxFins<Pdi2<FF','PZZZZdddZdinZiinZdnnZnnnZiddPZZZ','ddddinnn_ddd_ddd_ddd_ddd_ddddddi','PZZ__ZZPZddddddZZdiiiidZ_diiiid_ddiiiid_ZiiiiidZZdiddddZPZZ__ZZP','F<<2F<<2F<<2F<<2PFF<ZPPPxxddx\x82nd']
z1=[-33,-31,-18,-14,14,18,31,33]
z2=[-17,-16,-15,-1,1,15,16,17]
z3=[-17,-15,15,17]
z4=[-16,-1,1,16]
z5=[[],[],z1,z3,z4,z3+z4,z2]
z6=[15]*128
for x,y in((0,13),(7,14),(4,12),(112,7),(119,11),(116,3)):z6[x]=y
B=bytearray(128);S=0;C=0;E=-1;V=0;U=[];N=0;G=200000;T={};K=[[0,0]for _ in range(256)];H=[0]*32768;W=0;X=0;R=set();M=100000;KW=4;KB=116
class Y(Exception):pass
def J(p,s):
 t=p-6*(p>6);r=s>>4;f=s&7;w=(7-r)if p<=6 else r;z=P0[t-1]
 x=A[t]+ord(z[w*8+f if t==5 else w*4+(f if f<4 else 7-f)])-100
 return x if p<=6 else-x
def s(o):
 global S,C,E,V,KW,KB,W,X
 for i in range(128):B[i]=13 if i&0x88 else 0
 q=o.split();V=0;W=0;X=0
 for r,a in enumerate(q[0].split('/')):
  f=0
  for b in a:
   if b.isdigit():f+=int(b)
   else:
    p='PNBRQK'.index(b.upper())+1
    if b.islower():p+=6
    t=(7-r)*16+f;B[t]=p
    if p==6:KW=t
    elif p==12:KB=t
    if p==3:W+=1
    elif p==9:X+=1
    V+=J(p,t);f+=1
 if W>=2:V+=30
 if X>=2:V-=30
 S=0 if q[1]=='w' else 1
 C=0
 for b in q[2]:C|={'K':1,'Q':2,'k':4,'q':8}.get(b,0)
 E=-1 if q[3]=='-' else(ord(q[3][0])-97)+(int(q[3][1])-1)*16
def a(s,w):
 h=0 if w else 6;o=1 if w else-1
 for d in(-15*o,-17*o):
  t=s+d
  if not(t&0x88)and B[t]==1+h:return 1
 for q,D in((2,z1),(6,z2)):
  for d in D:
   t=s+d
   if not(t&0x88)and B[t]==q+h:return 1
 for q,D in((3,z3),(4,z4)):
  for d in D:
   t=s+d
   while not(t&0x88):
    p=B[t]
    if p:
     if p==q+h or p==5+h:return 1
     break
    t+=d
 return 0
def c():return a(KW if S==0 else KB,S==1)
def g(w=0):
 m=[]
 for f in range(128):
  if f&0x88:continue
  p=B[f]
  if not p or p==13 or(p<=6)!=(S==0):continue
  t=p-6*(p>6)
  if t==1:
   e=16 if S==0 else-16
   q=f+e
   if(not w or(q>>4)in(0,7))and B[q]==0:
    if(q>>4)in(0,7):
     for o in(5,4,3,2):m.append(f|(q<<7)|(o<<14))
    else:
     m.append(f|(q<<7))
     if(f>>4)==(1 if S==0 else 6):
      v=f+2*e
      if B[v]==0:m.append(f|(v<<7))
   for d in(e-1,e+1):
    q=f+d
    if q&0x88:continue
    v=B[q]
    if(v and v!=13 and(v<=6)!=(S==0))or q==E:
     if(q>>4)in(0,7):
      for o in(5,4,3,2):m.append(f|(q<<7)|(o<<14))
     else:m.append(f|(q<<7))
  else:
   for d in z5[t]:
    q=f+d
    while not(q&0x88):
     v=B[q]
     if v==0:
      if not w:m.append(f|(q<<7))
     elif v!=13 and(v<=6)!=(S==0):m.append(f|(q<<7));break
     else:break
     if t==2 or t==6:break
     q+=d
 if not w:
  for r,e,k,f2,t2,y in((1,(5,6),4,7,6,(4,5,6)),(2,(3,2,1),4,0,2,(4,3,2)),(4,(117,118),116,119,118,(116,117,118)),(8,(115,114,113),116,112,114,(116,115,114))):
   if C&r and(k==4)==(S==0)and B[f2]==(4 if k==4 else 10)and all(B[x]==0 for x in e)and all(not a(x,k==116)for x in y):m.append(k|(t2<<7))
 return m
def k(m):
 global S,C,E,V,KW,KB,W,X
 f=m&127;t=(m>>7)&127;o=m>>14;p=B[f];q=B[t]
 U.append((m,q,C,E,V,KW,KB,W,X))
 V-=J(p,f)
 if q:
  V-=J(q,t)
  if q==3:
   if W==2:V-=30
   W-=1
  elif q==9:
   if X==2:V+=30
   X-=1
 if o==3:
  if S==0:
   if W==1:V+=30
   W+=1
  else:
   if X==1:V-=30
   X+=1
 if(p==1 or p==7)and t==E and q==0:
  v=t-16 if p==1 else t+16;V-=J(B[v],v);B[v]=0
 B[t]=(o+6 if S==1 else o)if o else p;B[f]=0;V+=J(B[t],t)
 if p==6 or p==12:
  d={(4,6):(7,5),(4,2):(0,3),(116,118):(119,117),(116,114):(112,115)}.get((f,t))
  if d:
   r,w=d;B[w]=B[r];B[r]=0;V-=J(4 if p==6 else 10,r);V+=J(4 if p==6 else 10,w)
 if p==6:KW=t
 elif p==12:KB=t
 C&=z6[f]&z6[t]
 E=(f+t)//2 if(p==1 or p==7)and abs(t-f)==32 else-1
 S=1-S
def u():
 global S,C,E,V,KW,KB,W,X
 m,q,C,E,V,KW,KB,W,X=U.pop()
 f=m&127;t=(m>>7)&127;o=m>>14;p=B[t]
 if p==6 or p==12:
  d={(4,6):(7,5),(4,2):(0,3),(116,118):(119,117),(116,114):(112,115)}.get((f,t))
  if d:
   r,w=d;B[r]=B[w];B[w]=0
 B[f]=(1 if S==1 else 7)if o else p
 if(B[f]==1 or B[f]==7)and t==E and q==0:
  v=t-16 if B[f]==1 else t+16;B[v]=7 if B[f]==1 else 1
 B[t]=q;S=1-S
def o(m,n,ply):
 f=m&127;t=(m>>7)&127
 if m==n:return 1<<20
 q=B[t]
 if q:return(10*A[q]-A[B[f]]//10)+(1<<18)
 if m==K[ply][0]:return 1<<16
 if m==K[ply][1]:return 1<<15
 if B[t]==0 and not(m>>14):return H[S*16384+f*128+t]
 return 0
def l(m):
 k(m);b=a(KW if S==1 else KB,S==0)
 if b:u()
 return not b
def search(d,a,b,ply):
 global N,S,E
 N+=1
 if(N&2047)==0 and N>G:raise Y
 k=bytes(B)+bytes((C,E+1,S))
 if k in R:return 0
 e=T.get(k);n=0
 if e:
  r2,r3,r4,r5=e;n=r5
  if r2>=d:
   s=r4-ply if r4>99000 else(r4+ply if r4<-99000 else r4)
   if r3==0:return s
   if r3==1 and s>=b:return s
   if r3==2 and s<=a:return s
 if d<=0:return Q(a,b,ply)
 R.add(k)
 try:
  h=c();d+=h
  if d>=3 and not h:
   x,y2=S,E;S,E=1-S,-1
   s=-search(d-4 if d>=6 else d-3,-b,-b+1,ply+1)
   S,E=x,y2
   if s>=b:return b
  m1=g()
  m2=[(-o(m,n,ply),m)for m in m1]
  m2.sort()
  m3=-M;m4=0;m5=2;r6=a;m6=0
  for _,m in m2:
   q=B[(m>>7)&127]
   if d<2 and m6 and not q and not(m>>14) and not h and((m>>7)&127)!=E and(V if S==0 else-V)+150<=a:continue
   if not l(m):continue
   m6+=1;m8=q==0 and not(m>>14);m9=0
   if d>=3 and m6>3 and m8 and not h:m9=2 if(d>=5 and m6>8)else 1
   x=-r6-1 if m6>1 else-b
   s=-search(d-1-m9,x,-r6,ply+1)
   if s>r6:
    if m9:s=-search(d-1,x,-r6,ply+1)
    if s>r6 and m6>1:s=-search(d-1,-b,-r6,ply+1)
   u()
   if s>m3:m3=s;m4=m
   if s>r6:
    r6=s;m5=0
    if r6>=b:
     if m8:
      K[ply][1]=K[ply][0];K[ply][0]=m;H[S*16384+(m&127)*128+((m>>7)&127)]+=d*d
     m5=1;break
  if m4==0:return-M+ply if h else 0
  r4=m3+ply if m3>99000 else(m3-ply if m3<-99000 else m3)
  T[k]=(d,m5,r4,m4)
  return m3
 finally:R.discard(k)
def Q(a,b,ply):
 global N
 N+=1
 if(N&2047)==0 and N>G:raise Y
 n=V if S==0 else-V
 if n>=b:return b
 if n>a:a=n
 if ply>60:return a
 m1=g(w=not c())
 m2=[(-o(m,0,ply),m)for m in m1]
 m2.sort()
 for _,m in m2:
  t=(m>>7)&127;q=B[t]
  if q and not(m>>14)and n+A[q]+200<a:continue
  if q and not(m>>14):
   v=B[m&127]
   if A[v]>800 and A[q]+200<A[v]:continue
  if not l(m):continue
  s=-Q(-b,-a,ply+1);u()
  if s>a:
   a=s
   if a>=b:break
 return a
def v(m):
 f=m&127;t=(m>>7)&127
 u=chr((f&7)+97)+str((f>>4)+1)+chr((t&7)+97)+str((t>>4)+1)
 return u+('nbrq'[(m>>14)-2]if m>>14 else'')
def Z(o2):
 global N,H,C,E,V,KW,KB,W,X,S
 N=0;T.clear();H=[0]*32768
 for i in range(256):K[i][0]=K[i][1]=0
 o1=[]
 for w in o2:
  f=(ord(w[0])-97)+(int(w[1])-1)*16
  t=(ord(w[2])-97)+(int(w[3])-1)*16
  o=0
  if len(w)==5:o={'n':2,'b':3,'r':4,'q':5}[w[4]]
  o1.append(f|(t<<7)|(o<<14))
 b=o1[0];order=list(o1)
 B0=bytes(B);z0=(C,E,V,KW,KB,W,X,S);u0=len(U)
 try:
  for d in range(1,64):
   n7=[];n8=b;n9=-M
   for j,m in enumerate(order):
    k(m)
    if j==0:s=-search(d-1,-M,M,1)
    else:
     s=-search(d-1,-n9-1,-n9,1)
     if s>n9:s=-search(d-1,-M,-n9,1)
    u()
    n7.append((-s,m))
    if s>n9:n9=s;n8=m
   b=n8;n7.sort();order=[m for _,m in n7]
 except Y:
  B[:]=B0;C,E,V,KW,KB,W,X,S=z0;del U[u0:]
 return v(b)
z7=None
def O(path,o3):
 global z7
 if z7 is None:
  z7=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("MAKEFUN_ENV_URL is not set")
 q=w.Request(z7+path,json.dumps(o3).encode(),headers={"content-type":"application/json"})
 try:
  with w.urlopen(q)as r:return json.load(r)
 except Exception as e:sys.exit(e)
def n():
 while 1:
  g=O("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   s(g["fen"]);g=O("/move",{"game":g["game"],"move":Z(g["legal_moves"])})
if __name__=="__main__":n()
