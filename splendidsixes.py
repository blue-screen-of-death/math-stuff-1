import random
done = {''}
ops = ['+', '-', '*', '/', '%']
def randEquation(arg, res):
    equation = str(arg)
    for i in range(0, arg-1):
        r = random.randint(0, 4)
        op = ops[r]
        equation += op+str(arg)
    if eval(equation) == res and not equation in done:
        print(equation)
        done.add(equation)
while True:
    i = input('Choose a starting number (e.g 6 for splendid sixes): ')
    j = input('Choose a result number (e.g 3 for splendid sixes): ')
    print('Hit Ctrl+C to stop generating expressions.');
    try:
        while True:
                randEquation(int(i), int(j))
    except KeyboardInterrupt:
        continue
