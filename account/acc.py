from datetime import datetime as dt
today = dt.now().strftime("%Y-%b-%d")

class AddaAccount:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def loss(self, amount):
        self.balance=self.balance - amount
    
    def profit(self, amount):
        self.balance=self.balance + amount
    
    def replace(self, amount):
        self.balance=amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class SpartanAccount:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def loss(self, amount):
        self.balance=self.balance - amount
    
    def profit(self, amount):
        self.balance=self.balance + amount
    
    def replace(self, amount):
        self.balance=amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

account=AddaAccount("adda52balance.txt")
print("Your current Adda52 balance = "+str(account.balance))
account1=SpartanAccount("spartanbalance.txt")
print("Your current Spartan balance = "+str(account1.balance))

while True:
    print("Update Adda52 balance? y or n")
    input1 = input()
    input1 = input1.lower()
    if input1 == "y":
        print("Enter your new Adda52 balance:")
        newAdda = int(input())
        account.replace(newAdda)
        account.commit()
        account.balance="{:,}".format(account.balance)
        print("Your new Adda52 balance is: "+str(account.balance)+" on "+today+".")
        break
    elif input1 == "n":
        break
    else:
        print("Let me ask you again.")

while True:
    print("Update Spartan balance? y or n")
    input2 = input()
    input2 = input2.lower()
    if input2 == "y":
        print("Enter your new Spartan balance:")
        newSpartan = int(input())
        account1.replace(newSpartan)
        account1.commit()
        account1.balance="{:,}".format(account1.balance)
        print("Your new Spartan balance is: "+str(account1.balance)+" on "+today+".")
        break
    elif input2 == "n":
        break
    else:
        print("Let me ask you again.")

### second method with  while loops
# while True:
#     print("Enter Adda profit/loss (or type quit):")
#     input1 = int(input())
#     if input1 == 0:
#         break
#     else:
#         account.profit(input1)
#         account.commit()
#         account.balance = "{:,}".format(account.balance)
#         print("Your new Adda52 balance is: "+account.balance+" on "+today+".")
#         break
# 
# while True:
#     print("Enter Spartan profit/loss:")
#     input2 = int(input())
#     if input2 == 0:
#         break
#     else:
#         account1.profit(input2)
#         account1.commit()
#         account1.balance = "{:,}".format(account1.balance)
#         print("Your new Spartan balance is: "+account1.balance+" on "+today+".")
#         break

### first method with only
#while True:
#    print("Did you win? y or n\nType 'quit' to quit.")
#    input1 = input()
#    input1 = input1.lower()
#    if input1 == "y":
#        dep = int(input("How much?\n"))
#        account.profit(dep)
#        account.commit()
#        account.balance = "{:,}".format(account.balance)
#        print("Your new Adda52 balance is: "+account.balance+" on "+today+".")
#        break
#    elif input1 == "n":
#        print("You lose, right? y or n")
#        input2 = input()
#        input2 = input2.lower()
#        if input2 == "y":
#            withDraw = int(input("How much?\n"))
#            account.loss(withDraw)
#            account.commit()
#            account.balance = "{:,}".format(account.balance)
#            print("Your new Adda52 balance is: "+str(account.balance)+" on "+today+".")
#            break
#        elif input2 == "n":
#            #print("cy@")
#            account.balance = "{:,}".format(account.balance)
#            print("Your Adda52 balance is still: "+str(account.balance)+" on "+today+".")
#            break
#        else:
#            print("I'm sorry, I don't understand that.")
#            account.balance = "{:,}".format(account.balance)
#            print("Your Adda52 balance is still: "+str(account.balance)+" on "+today+".")
#            break
#    elif input1 == "quit":
#        account.balance = "{:,}".format(account.balance)
#        print("Your Adda52 balance is still: "+str(account.balance)+" on "+today+".")
#        break
#    else:
#        print("I'm sorry, I don't understand that.")
