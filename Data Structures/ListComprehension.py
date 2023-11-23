def invert_negative_num (negative_num):
  positive_num = negative_num*-1
  return positive_num



transactions_in_cents = [1000, -450, 7500, -3475, 13000, -8150, 25000, -850, 0, -1125, -600, 102550, -25025, 6500, -3850, -2500, 1875, 4000]

print("Transactions (cents):") 
print(transactions_in_cents)

transactions = [transactions/100 for transactions in transactions_in_cents]
transactions.sort()

print("Sorted Transaction(Dollars):")
print(transactions)

deposits=[transaction for transaction in transactions if transaction >=0]
print("Deposits:")
print(deposits)


withdrawals=[trans for trans in transactions if trans <0]
withdrawals = [invert_negative_num(trans) for trans in withdrawals]

print("Withdrawals (positive values):") 
print(withdrawals)

largest_withdrawals = withdrawals[:5]
print("Largest Withdrawals:")
print(largest_withdrawals)

average_deposit = int(sum(deposits)/len(deposits))
average_withdrawal= int(sum(withdrawals)/len(withdrawals))

balance = sum(transactions)
print("Balance:")
print(balance)