print("Welcome to bus station ☻") 
print("1. Al Nasr Street ") 
print("2. Al Wahda Street ") 
print("3. Al Galaa Street ") 
print("4. Salah Al , Din Street ") 
print("5. Al Rasheed Street ") 
 
a=int(input("Enter the number of your distination : ")) 
if a == 1: 
    print("The bus will go to Al Nasr Street after 30 minutes") 
elif a == 2: 
    print("The bus will go to Al Wahda Street after 15 minutes") 
elif a == 3: 
    print("The bus will go to Al Al Galaa Street after 25 minutes") 
elif a == 4: 
    print("The bus will go to Salah Al , Din Street after 35 minutes") 
elif a == 5: 
    print("The bus will go to Al Rasheed Street after 10 minutes") 
else: 
    print("Enter Number of thes Buses"); 
 
print("Do you wanna book a place? \nfor yes enter 1\nfor no press 2") 
print("Enter 1 To Booking Confirmation") 
print("Enter 2 To Cancellation") 
b = int(input("")); 
if b==1: 
    print("Your chair number is 8 The bus will move soon.") 
    print("The number of Available Chairs is 20") 
    print("The number of booked Chairs is 30") 
     
if b==2: 
    print("Thank you ☺")