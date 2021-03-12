
#  simple Interest
#  si = p * T * /100


def interest(Value1, Value2, Value3):
    si = (Value1 * Value2 * Value3)/100
    print("The simple interest of above numbers", si)
    return si
Principal = int( input( "Please enter your principal amount :" ) )
Time = int( input( "Please enter your time:" ) )
Rate = int( input( "Please enter your rate:" ) )
interest( Principal, Time, Rate )


# A = P(1 + R/100) t
# Compound Interest = A – P

def compoundinterest(principal,rate,time):
    amount = principal * (pow((1+ rate / 100),time))
    print( "The total amount is", amount )
    ci = amount - principal
    print("The compound interest is:", ci)
compoundinterest( 10, 20, 30 )