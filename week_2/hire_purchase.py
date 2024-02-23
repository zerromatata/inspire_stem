# Program to calculate hire purchase
# Date : 21/02/2024
# Name : zerro


CP = float(input("Enter cost price"))
deposit1 = float(input("Enter the deposit percentage"))
installments = float(input("Enter the number of installments"))
pinstallments = float(input("Enter price of each installments"))
deposit2 = deposit1 * 0.01
downpayment = deposit2 * CP
hirepurchase = downpayment + installments * pinstallments

print(hirepurchase)

additionalprice1 = hirepurchase - CP
additionalprice2 = additionalprice1 * 100/CP

print(additionalprice1 ,"is the additional price he is paying",)
print(additionalprice2 ,"is the percentage of the additional price he is paying")