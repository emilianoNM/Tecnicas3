x1=1
x2=1.8
x3=2
x4=2.5
x5=3
x6=5
x7=15.3
y1=1
y2=1.5
y3=2.5
y4=2.8
y5=4
y6=6
y7=17.8
exispory=x1*y1+x2*y2+x3*y3+x4*y4+x5*y5+x6*y6+x7*y7
sumx=x1+x2+x3+x4+x5+x6+x7
sumy=y1+y2+y3+y4+y5+y6+y7
exiscua=x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2
sumxcua=sumx**2
A=(7*exispory-sumx*sumy)/(7*exiscua-sumxcua)
B=(sumy-A*sumx)/7
print ('Y=',A,'*X+',B) 
