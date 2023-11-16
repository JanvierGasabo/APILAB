def Calc_SumOfMultiples(limit):
    a=list()
    for num in range(limit):
        if num %3==0 or num % 5==0:
            a.append(num)
    print(a)
    return sum(a)
        
number= int(input("Enter a limit number to start : "))    
result=Calc_SumOfMultiples(number)
print(result)
      

