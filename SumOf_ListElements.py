def SumOfList(size):
    numbers=list()
    for i in range(size):
        element=int(input(f"enter number {i +1}  to add :"))
        numbers.append(element)
    print(numbers)
    return sum(numbers)
size=int(input("enter size:"))
print(SumOfList(size))    
    
  
