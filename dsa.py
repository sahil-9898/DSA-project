print("********************STOCK MARKET SIMULATOR********************\n")
print()
from nsetools import Nse
nse=Nse()
from pprint import pprint


inventory=[]
cash=10000000
running=True
while running:
    print("\nSelect from the following options\n1. Search stock\n2. View Account Balance\n3. Add funds\n4. Withdraw Funds\n5. Open Inventory\n6. Exit\n")
    user=int(input())
    
    if user==6:
        running=False
        break
    
    elif user==2:
        print("Your account balance is: ",cash)

    elif user==3:
        print("Enter amount: ")
        addamount=int(input())
        cash+=addamount
        print("New account balance is: ",cash)

    elif user==4:
        print("Enter amount: ")
        withdrawamount=int(input())
        cash-=withdrawamount
        print("New account balance is: ",cash)

    elif user==1:
        print("Enter the code for desired stock\n")
        stockname=input()
        stockvalidity=nse.is_valid_code(stockname)
        if stockvalidity==False:
            print("The code is not valid")
        else:
            stockdetails=nse.get_quote(stockname)
            print(stockdetails['companyName'],'\n')
            print(stockdetails['secDate'],'\n')
            print("Current price: ",stockdetails['buyPrice1'])
            print("Average price: ",stockdetails['averagePrice'])
            print("Day High: ",stockdetails['dayHigh'])
            print("Day Low: ",stockdetails['dayLow'])
            print("Previous Close: ",stockdetails['previousClose'])
            print("Year High: ",stockdetails['high52'])
            print("Year Low: ",stockdetails['low52'],'\n')
            print("Buy stock (yes/no): ")
            buy=input()
            if buy=="no":
                continue
            else:
                print("Enter number of stocks: ")
                lot=int(input())
                cost=stockdetails['buyPrice1']
                totalcost=lot*cost
                print("Total cost will be: ",totalcost)
                print("Your account balance is",cash)
                print("Do you wish to continue? (yes/no): ")
                trade=input()
                if trade=="no":
                    print("Transaction cancelled")
                    continue
                else:
                    if totalcost>cash:
                        print("Insufficient balance")
                    else:
                        cash-=totalcost
                        inventory.append([stockname,cost,lot])
                        print("Transaction successfull")

    elif user==5:
        print(inventory)
        #yaha se aage launde karenge
        #inventory naam ki list hai list ke andar jo stock buy kiya hai uska naam kis price par buy kiya hai or kitne stocks buy kiye ye available hoga
        #using that data net profit loss and sell option and most important..... data structure use karna baaki hai
                
            




