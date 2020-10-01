print (

'''
╔═══╗──╔╗──────╔╗───╔╗
║╔═╗║──║║──────║║──╔╝╚╗
║║─╚╬══╣║╔══╦╗╔╣║╔═╩╗╔╬══╦═╗
║║─╔╣╔╗║║║╔═╣║║║║║╔╗║║║╔╗║╔╝
║╚═╝║╔╗║╚╣╚═╣╚╝║╚╣╔╗║╚╣╚╝║║
╚═══╩╝╚╩═╩══╩══╩═╩╝╚╩═╩══╩╝
''') 

#first read this------------\
#                           |
#                           |
#                           /          
#                          √
'''
   print("Your_Calculation")
   print("for_addition : type 'add'")
   print("for_multiplication : 'multiply'")
   print("for_division : 'divide'")
   print("for_subtration :subtract")
   print("for_square_root: root")
   print("for_cancle_processing :'clear'")
'''  
while True:
   user_input = input()
   
   if user_input == "clear":
     break 
    
   elif user_input== 'add':
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter b number: "))
    result= (num1 +num2)
    print(result)
      
   elif user_input=='multiply':
     num1 =float(input(""))
     num2 =float(input(""))
     result=(num1*num2)
     print(result)
   elif user_input=='divide':
     num1 =float(input(""))
     num2 =float(input(""))
     result =(num1 //num2)
     print(result)

   elif user_input=='subtract':
     num1 =float(input(""))
     num2 =float(input(""))
     result =(num1 - num2)
     print(result)


   elif user_input=='root':
     num1 =float(input(""))
     num2 =float(input(""))
     result1 = (num1**1/2) 
     result2=  (num2**1/2) 
     print(result1)
     print(result2 )