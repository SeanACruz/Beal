#for j in range(2):
    #for i in range(5):
        #if i==2 or i==4:
            #print("i=",i+1)
#mylist=(1, 2, 3, 4, 5, 6)
#for i in mylist:
    #if (i % 3)==0: print(i)

import timeit

start = timeit.default_timer()

alistfile=open("C:\\Users\\acer\\Desktop\\Beallists\\alist.txt","r")                                         #alist= a (base)
alist=alistfile.read().split(',')
alistfile.close()



blist=range(1,10001)

xrange=range(3,10)                                                        #xrange= X (exponent)

ylist=range(3,10)                                                         #yrange= y (exponent)

c=2                                                                         #c= c (base)
for z in range(3,101):                                                    #z= z(exponent)
    cz=(c**z)
    for a in alist:
        a=int(a)
        for x in xrange:
            for b in blist:
                #b=int(b)
                for y in ylist:
                    if cz==((a**x)+(b**y)):
                       print(a,"^",x,"+",b,"^",y,"=",c,"^",z)

stop = timeit.default_timer()

print('Time: ', stop - start)