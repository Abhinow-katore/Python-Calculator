print(
'''
╔═══╗──╔╗──────╔╗───╔╗
║╔═╗║──║║──────║║──╔╝╚╗
║║─╚╬══╣║╔══╦╗╔╣║╔═╩╗╔╬══╦═╗
║║─╔╣╔╗║║║╔═╣║║║║║╔╗║║║╔╗║╔╝
║╚═╝║╔╗║╚╣╚═╣╚╝║╚╣╔╗║╚╣╚╝║║
╚═══╩╝╚╩═╩══╩══╩═╩╝╚╩═╩══╩╝
''') 

print("For addition : type 'add'")
print("Multiplication: 'multiply'")
print("Division: 'divide'")
print("Subtraction: 'subtract'")
print("Square root: 'root'")

while True:
   user_input = input("Enter command: ")
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
