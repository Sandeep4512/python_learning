cup_size = input("Please enter the cup size !").lower()
if cup_size =="small":
    price = 10
    print( f"You have selected a small cup size : {price}")
elif  cup_size == "medium":
    price = 15
    print(f"You have selected a medium cup size : {price}") 
elif cup_size == "large" :
    price = 20
    print(f"you have selected large cup size : {price}")
else :
    print(f"Please select the correct cup size ?")