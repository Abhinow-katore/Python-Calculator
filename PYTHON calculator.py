print(
'''
╔═══╗──╔╗──────╔╗───╔╗
║╔═╗║──║║──────║║──╔╝╚╗
║║─╚╬══╣║╔══╦╗╔╣║╔═╩╗╔╬══╦═╗
║║─╔╣╔╗║║║╔═╣║║║║║╔╗║║║╔╗║╔╝
║╚═╝║╔╗║╚╣╚═╣╚╝║╚╣╔╗║╚╣╚╝║║
╚═══╩╝╚╩═╩══╩══╩═╩╝╚╩═╩══╩╝
''') 

print("Your_Calculation")
print("for_addition : type 'add'")
print("for_multiplication : 'multiply'")
print("for_division : 'divide'")
print("for_subtration :subtract")
print("for_square_root: root")
print("for_cancle_processing :'clear'")

while True:
   user_input = input("Enter command: ")
   
   if user_input == "clear":
     break 
    
   elif user_input == 'add':
    num1 = float(input("Enter number a: "))
    num2 = float(input("Enter number b: "))
    result = num1 + num2
    print(result)
      
   elif user_input == 'multiply':
     num1 = float(input("Enter number a: "))
     num2 = float(input("Enter number b: "))
     result = num1 * num2
     print(result)
   elif user_input == 'divide':
     num1 =float(input("Enter number a: "))
     num2 =float(input("Enter number b:"))
     result = num1 / num2
     print(result)

   elif user_input == 'subtract':
     num1 = float(input("Enter number a: "))
     num2 = float(input("Enter number b: "))
     result = num1 - num2
     print(result)


   elif user_input == 'root':
     num1 = float(input("Enter number: "))
     result = num1 ** 0.5
     print(result)
     
   elif user_input == 'percentage':
     num1 = float(input("Enter number: "))
     result = num1 / 100)
     print(result1)
