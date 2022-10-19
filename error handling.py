#nums = ['1','2','3','4','5','6']

#try: 
    #print (sum(nums))

#except: 
#    print ('can not print')

#finally: 
#    print ('result')

try:
    a = [int(x) for x in input('enter numbers: ').split()]
    print (sum(a))
except: 
    print ('not numbers')
finally:
    print ('end')