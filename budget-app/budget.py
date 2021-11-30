class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []
  
  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({'amount': -amount, 'description': description})
      return True
    else:
      return False
  
  def get_balance(self):
    return sum([x.get('amount') for x in self.ledger])

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {category.category}')
      category.deposit(amount, f'Transfer from {self.category}')
      return True
    else:
      return False

  def check_funds(self, amount):
    return self.get_balance() >= amount

  def __str__(self):
    output = self.category.center(30, '*') + '\n'
    
    for i in self.ledger:
      output += f'{i.get("description")[:23]:23}{i.get("amount"):7.2f}\n'

    output += f'Total: {self.get_balance():.2f}'

    return output

def create_spend_chart(categories):
  output = 'Percentage spent by category\n'

  withdrawals = [-sum([x.get('amount') for x in category.ledger if x.get('amount') < 0]) for category in categories]

  withdrawal_percentages = [round(x / sum(withdrawals) * 100) for x in withdrawals]

  category_names = [category.category.lower().capitalize() for category in categories]

  for i in range(100, -10, -10):
    output += str(i).rjust(3) + '| '
    for percentage in withdrawal_percentages:
      output += 'o  ' if percentage >= i else '   '
    output += '\n'
  
  output += ' ' * 4 + '-' * (2 * (len(categories) + 1) + 2)
  length_of_longest_category_name = len(max(category_names, key=len))
  category_names = [x.ljust(length_of_longest_category_name) for x in category_names]

  for i in range(length_of_longest_category_name):
    output += '\n     '
    for category_name in category_names:
      output += category_name[i] + '  '

  return output