keep_going = 'y'

while keep_going == 'y':
  sales = float(input('enter sales:'))
  comm_rates = float(input('enter commision rates:'))

  commision = sales * comm_rate
print(f'The comission is ${comission:,.2f}.')

keep_going = input('DO you want to calculate another? ' + 'comission (enter y for yes): ')
