print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill?\n$'))
perc_tip = int(input('What percentage tip would you like to give?\n10, 12, 0r 15?\n'))
split_no = int(input('How many people would you like to split the bill amongst?\n'))
tip_as_percent = perc_tip / 100
tip_amount = tip_as_percent * total_bill
total_bill_to_pay = tip_amount + total_bill
# total_to_pay_per_person = round(total_bill_to_pay / split_no, 2)
total_to_pay_per_person = '{:.2f}'.format(total_bill_to_pay/split_no)
print(f'Each person should pay {total_to_pay_per_person}')
