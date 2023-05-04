def compute(n):
    if n < 10:
        out = n ** 2

# Original statement-> elif n < 20:
# Question was unclear whether to include 10 and 20 in the range or not 
# so I assumed that between means 10 and 20 are included
    elif n <= 20:
        out = 1

# Original statement-> for i in range(1, n-10):
# Increasing the range by 1 to include the last number
        for i in range(1, n-10+1):
            out *= i
    else:
        lim = n-20
# Original statement-> 
#       out = lim * lim
#       out = out - lim
#       out = out = 2 
# Couldn't make sense of what the above code was trying to do
# So I just included the last number in the range and calculated the sum from 1 to n-20
        out = 0
        for i in range(1, lim+1):
            out += i
    print(out)


n = int(input("Enter an integer: "))
compute(n)



