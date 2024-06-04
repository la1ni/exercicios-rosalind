k = 2 #AA
m = 2 #aa
n = 2 #Aa
total = k+m+n
cruzhomodom = (k/total) * (k-1)/(total-1) #AAAA kk
cruzhomorec = (m/total) * (m-1)/(total-1) #aaaa mm
cruzheterohetero = n/total * (n-1)/(total-1) #AaAa nn
cruzheterohomodom = n/total * (k)/(total-1) #AaAA nk
cruzheterohomorec = n/total * (m)/(total-1) #Aaaa nm
cruzheterodomrec = ((k+m)/total * (k+m-1-(k-1))/(total-1)) * 2 #AAaa km
soma =  cruzheterodomrec + cruzheterohetero + cruzheterohomorec +cruzheterohomodom + cruzhomorec + cruzhomodom
#print (soma)
AAAA = 1
aaaa = 0
AaAa = 3/4
AaAA = 1
Aaaa = 1/2
AAaa = 1
x = (AAAA*cruzhomodom) + (aaaa*cruzhomorec) + (AaAa*cruzheterohetero) + (AaAA*cruzheterohomodom)+ (Aaaa*cruzheterohomorec)+ (AAaa * cruzheterodomrec)
print(x)
