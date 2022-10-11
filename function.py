#def add_three(num1,num2,num3): 
#    sum_three= num1+num2+num3
#    return sum_three
#sum_output = add_three(1,2,3)
#print (sum_output)

#def div_four(num1,num2,num3):
#    total= num1/num2/num3
#    return total
#sum_output = div_four(3,3,3)
#print (sum_output)

#def cal(num1,add2,sub3,div4):
#    total = num1+(add2-sub3)/div4
#    return total
#sum_output = cal(1,2,3,4)
#print (sum_output)

def numbers(n):
    num_str = repr(n)
    last_digit_str = num_str[-1]
    last_digit = int(last_digit_str)
    if (last_digit %2) == 0:
        output = 'even'
    else:
        output = 'odd'
    print (output)
numbers(73204957)