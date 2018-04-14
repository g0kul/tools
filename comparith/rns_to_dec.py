#rns to decimal
#input: <given rns separated by space> <-1> <rns base separated by space>
# to input (1,2,3) base (5,6,7) RNS input below
# 1 2 3 -1 5 6 7

import sys
from functools import reduce

#print(sys.argv)

#truncate the file name
given = sys.argv[1:]

len_tot = len(given)

if(len_tot == 0):
    print("Enter number separated by space between residue and -1 between two numbers")
    exit(0)

#-1 is the divisor between given rns and the rns base
no_div_index = given.index('-1')

rns_in = given[:no_div_index]
rns_base = given[no_div_index+1:]

total_reps = 1

for i in range(no_div_index):
    rns_in[i] = int(rns_in[i])
    rns_base[i] = int(rns_base[i])
    total_reps = total_reps * rns_base[i]

#for signed
total_reps_neg = total_reps/2

#if total rep is odd, add one no to positive side else keep actual
total_reps_pos = total_reps_neg
if(total_reps %2 == 0):
    total_reps_pos = total_reps_pos-1

print("Input RNS Number: ",rns_in)
print("Input RNS Base: ",rns_base)
print("Total Unsigned Decimal Rep: 0 to %d" % (total_reps-1))
print("Total Signed Decimal Rep: -%d to %d" % (total_reps_neg, total_reps_pos))

sum = 0
residues = []

for i in range(no_div_index):
    rns_in_cpy = list(rns_in)
    multplier = rns_in_cpy.pop(i)

    #print(rns_in_cpy)
    #print(multplier)

    rns_base_cpy = list(rns_base)
    mod = rns_base_cpy.pop(i)

    # print(rns_base_cpy)
    # print(mod)

    start = reduce(lambda x, y: x*y, rns_base_cpy)
    #print(start)

    n = 1
    num = 0
    while True:
        num = n*start
        if(num % mod == 1):
            break
        else:
            n = n+1

    sum = sum + num*multplier
    residues.append(num)

    #print ("location : %d, mul: %d, val: %d" % (i,num,num*multplier))

print("Residues: ", residues)

udecimal = sum%total_reps
#print("raw", decimal)

#to get the negative number
if(udecimal > total_reps_pos):
    #decimal = decimal - total_reps_pos
    sdecimal = udecimal - total_reps

print ("Sum: %d, Signed Decimal: %d" % (sum, sdecimal))
print ("Unsigned Decimal: %d, Signed Decimal: %d" % (udecimal, sdecimal))