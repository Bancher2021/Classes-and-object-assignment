
     
class Budget:
    def __init__(self, Food, Clothing, Entertainment):
        self.Food = Food
        self.Clothing = Clothing
        self.Entertainment = Entertainment
    def categories(self):
        print('select category')
        print('1. Food category')
        print('2. Clothing category')
        print('3. Entertainment category')
        selectedOption = int(input('please select an option \n'))
        if (selectedOption == 1):
            print('Please what do you want to do?:')
            print('1. Deposite')
            print('2. Withdraw')
            print('3. Transfer')
            selectedOption = int(input('please select an option \n'))
            if (selectedOption == 1):
                amount = int(input("Enter amount you want to Deposite: \n "))
                print('You deposited ', amount , 'into food cathegory')
            elif(selectedOption == 2):
                amount = int(input("Enter amount to be Withdrawn: \n"))
                if self.Food >= amount:
                    self.Food -= amount
                    print("\n You Withdrew:", amount)
                    print('Your balance is: ', self.Food)
                else:
                    print("\n Insufficient balance  ")
            elif(selectedOption == 3):
                print('Which category do you want to transfer to?')
                print('1. Clothing')
                print('2. Entertainment')
                selectedOption = int(input('please select an option \n'))
                if (selectedOption == 1):
                    Clothing = self.Food
                    print('you transfered', Clothing, 'to clothing category')
                elif(selectedOption == 2):
                    Entertainment = self.Food
                    print('you transfered ', Entertainment, 'to entertainment category')



                
        elif(selectedOption == 2):
             print('Please what do you want to do?:')
             print('1. Deposite')
             print('2. Withdraw')
             print('3. Transfer')
             selectedOption = int(input('please select an option \n'))
             if (selectedOption == 1):
                 amount = int(input("Enter amount you want to Deposite: \n "))
                 print('You deposited ', amount , 'into Clothing cathegory')

             elif(selectedOption == 2):
                 amount = int(input("Enter amount to be Withdrawn: \n"))
                 if self.Clothing >= amount:
                    self.Clothing -= amount
                    print("\n You Withdrew:", amount)
                    print('Your balance is: ', self.Clothing)
                 else:
                    print("\n Insufficient balance  ")
             elif(selectedOption == 3):
                print('Which category do you want to transfer to?')
                print('1. Food')
                print('2. Entertainment')
                selectedOption = int(input('please select an option \n'))
                if (selectedOption == 1):
                    Food = self.Clothing
                    print('you transfered', Food , 'to Food category')
                elif(selectedOption == 2):
                    Entertainment = self.Clothing
                    print('you transfered ', Entertainment, 'to entertainment category')



        elif(selectedOption == 3):
             print('Please what do you want to do?:')
             print('1. Deposite')
             print('2. Withdraw')
             print('3. Transfer')
             selectedOption = int(input('please select an option \n'))
             if (selectedOption == 1):
                 amount = int(input("Enter amount you want to Deposite: \n "))
                 print('You deposited ', amount , 'into Entertainment cathegory')

             elif(selectedOption == 2):
                 amount = int(input("Enter amount to be Withdrawn: \n"))
                 if self.Entertainment >= amount:
                    self.Entertainment -= amount
                    print("\n You Withdrew:", amount)
                    print('Your balance is: ', self.Entertainment)
                 else:
                    print("\n Insufficient balance  ")
             elif(selectedOption == 3):
                print('Which category do you want to transfer to?')
                print('1. Food')
                print('2. Clothing')
                selectedOption = int(input('please select an option \n'))
                if (selectedOption == 1):
                    Food = self.Entertainment
                    print('you transfered', Food , 'to clothing category')
                elif(selectedOption == 2):
                    clothing = self.Entertainment
                    print('you transfered ', Clothing , 'to entertainment category')

        else:
            print('Wrong option')

        


p1 = Budget(100, 200, 500) 
p1.categories()


     



