def arithmetic_arranger(problems, print_answers=False):
  
  # Get all operants
  operants = get_operants(problems)

  # Get all operators
  operators = get_operators(problems)

  # Validate input
  error = validate_input(problems, operants, operators)
  if error:
    return error  

  top_row = ""
  dashes = ""
  values = list(map(lambda x: eval(x), problems))
  solutions = ""
  
  for i in range(0, len(operants), 2):
    space_between = max(len(operants[i]), len(operants[i + 1])) + 2
    top_row += operants[i].rjust(space_between)
    dashes += '-' * space_between
    solutions += str(values[i // 2]).rjust(space_between)
    if i != len(operants) -2:
      top_row += ' ' * 4
      dashes += ' ' * 4
      solutions += ' ' * 4
  
  bottom_row = ""
  for i in range(1, len(operants), 2):
    space_between = max(len(operants[i - 1]), len(operants[i])) + 1
    bottom_row += operators[i // 2]
    bottom_row += operants[i].rjust(space_between)
    if i != len(operants) - 1:
      bottom_row += ' ' * 4

  if print_answers:
    return '\n'.join((top_row, bottom_row, dashes, solutions))
  else:
    return '\n'.join((top_row, bottom_row, dashes))


def get_operants(problems):
  
  output = []
  
  for problem in problems:
    parts = problem.split()
    output.extend([parts[0], parts[2]])
  
  return output


def get_operators(problems):
  return list(map(lambda x: x.split()[1], problems))


def validate_input(problems, operants, operators):

  # Only allow 5 problems at max
  if len(problems) > 5:
    return "Error: Too many problems."

  # Only allow '+' or '-' as operators
  if not all(map(lambda x: x == '+' or x == '-', operators)):
    return "Error: Operator must be '+' or '-'."

  # Only allow digits
  if not all(map(lambda x: x.isdigit(), operants)):
    return "Error: Numbers must only contain digits."

  # Only allow operants with 4 digits at max
  if not all(map(lambda x: len(x) <= 4, operants)):
    return "Error: Numbers cannot be more than four digits."