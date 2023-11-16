price= int(input("Enter the item price ==== "))
if price>=300:
    discountedPrice= price-price*30/100
    discount=price*30/100
    print("Dicounted price is equal to : ",discountedPrice)
    print("Your discount was ===>>>",discount)
elif price >= 200 and price < 300:
    discountedPrice=price-price*20/100
    discount=price*20/100
    print(" Discounted price is equal :" ,discountedPrice)
    print("Your discount was ===>>>",discount)
elif price >= 100 <200:
    discountedPrice=price-price*10/100
    discount=price*10/100
    print("Dicounted price is equal :",discountedPrice)
    print("Your discount was ===>>>",discount)
elif price>= 0  <100:
    discountedPrice=price-price*5/100
    discount=price*5/100
    print("Dicsounted price is equal to : ",discountedPrice)
    print("Your discount was ===>>>",discount)
elif price <0:
    discountedPrice=price
    print("No discount , The price is Negative ::",price)

