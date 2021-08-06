import re

def arithmetic_arranger(problems, calc):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    splits = []
    operands = []
    operators = []
    i = 1

    for problem in problems:
        splits.append(problem.split())

    for op in splits:
      if i % 2 == 0:
        if op == '+' or op == '-':
          operators.append(op)
        else:
          return 'Error: Operator must be ''+'' or ''-''.'
      else:
        if re.match(r'^([\d]+)$', op):
          if len(op) > 4:
            return 'Error: Numbers cannot be more than four digits.'
          operands.append(int(op))
        else:
          return 'Error: Numbers must only contain digits.'

      i += 1

    if calc:
      results = []
      i = 0
      for operator in operators:
        if operator == '+':
          results.append(operands[i] + operands[i+1])
        else:
          results.append(operands[i] - operands[i+1])
          
        i += 2
      



    return arranged_problems
