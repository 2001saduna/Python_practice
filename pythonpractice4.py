def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    #if else statement 
    count = 0
    while num !=0:
        if num % 2 ==0:
            num = num/2
            count += 1
        else:
            num = num -1
            count += 1
    print(count)
        
numberOfSteps(8)