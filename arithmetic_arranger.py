def arithmetic_arranger(problems, calc=None):
    if len(problems) <= 5:
        top = []
        bot = []
        operators = []
        dashes = []
        results = []

        for problem in problems:
            splits = problem.split()
            if splits[1] != "+" and splits[1] != "-":
                return "Error: Operator must be '+' or '-'."

            if not (splits[0].isnumeric()) or not (splits[2].isnumeric()):
                return "Error: Numbers must only contain digits."

            if len(splits[0]) > 4 or len(splits[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'

            if calc:
                if splits[1] == '+':
                    results.append(str(int(splits[0]) + int(splits[2])))
                else:
                    results.append(str(int(splits[0]) - int(splits[2])))

            operators.append(splits[1])
            top.append(str(splits[0]))
            bot.append(str(splits[2]))

        i = 0

        for operator in operators:
            if len(top[i]) < len(bot[i]):
                multiplier = (len(bot[i]) + 2) - len(top[i])

                top[i] = ' ' * multiplier + top[i]
                bot[i] = operator + ' ' + bot[i]
            else:
                top[i] = '  ' + top[i]
                multiplier = len(top[i]) - len(bot[i])
                bot[i] = operator + ' ' * (multiplier - 1) + bot[i]

            if calc:
                if len(top[i]) > len(results[i]):
                    multiplier = len(top[i]) - len(results[i])
                    results[i] = ' ' * multiplier + results[i]

                    dashes.append('-' * len(top[i]))
                else:
                    multiplier = len(results[i]) - len(top[i])
                    top[i] = ' ' * multiplier + top[i]
                    multiplier = len(results[i]) - len(bot[i])
                    bot[i] = operator + ' ' * multiplier + bot[i]

                    dashes.append('-' * (len(results[i]) + 1))
            else:
                dashes.append('-' * len(top[i]))

            i += 1

        arranged_problems = '    '.join(top) + '\n'
        arranged_problems += '    '.join(bot) + '\n'
        arranged_problems += '    '.join(dashes)

        if calc:
            arranged_problems += '\n' + '    '.join(results)

        return arranged_problems

    return 'Error: Too many problems.'
