import math

z = [12,16,20,24,32]

bk_c=[]
ks_c = []
hy_c = []
bk_d=[]
ks_d = []
hy_d = []
for x in z:
    bk_c.append(2*x-2-math.log(x,2))
    ks_c.append(x*math.log(x,2)-x+1)
    hy_c.append((x/2)*math.log(x,2))
    bk_d.append(2*math.log(x,2)-2)
    ks_d.append(math.log(x,2))
    hy_d.append(math.log(x,2)+1)



for x in range(len(z)):         
    print('Brent Kung : inp: %d, cost: %f'%(z[x],bk_c[x]))
    print('Kogge Stone: inp: %d, cost: %f'%(z[x],ks_c[x]))
    print('Hybrid Para: inp: %d, cost: %f'%(z[x],hy_c[x]))
    print('\n')

for x in range(len(z)):  
    print('Brent Kung : inp: %d, dly: %f'%(z[x],bk_d[x]))
    print('Kogge Stone: inp: %d, dly: %f'%(z[x],ks_d[x]))
    print('Hybrid Para: inp: %d, dly: %f'%(z[x],hy_d[x]))
    print('\n')

for x in range(len(z)):  
    print('Brent Kung : inp: %d, cost-dly: %f'%(z[x],bk_c[x] * bk_d[x]))
    print('Kogge Stone: inp: %d, cost-dly: %f'%(z[x],ks_c[x] * ks_d[x]))
    print('Hybrid Para: inp: %d, cost-dly: %f'%(z[x],hy_c[x] * hy_d[x]))
    print('\n')