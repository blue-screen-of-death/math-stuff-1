import random
ops = ['+', '-', '*', '/', '%']
done = {''}
while True:
    nums = ['2', '5', '9']
    r = random.randint(0, 2)
    equation = str(nums[r])
    nums.pop(r)
    r = random.randint(0, 1)
    q = random.randint(0, 4)
    equation += ops[q]+str(nums[r])
    nums.pop(r)
    r = random.randint(0, 0)
    q = random.randint(0, 4)
    equation += ops[q]+str(nums[r])
    nums.pop(r)
    if eval(equation)//1 == eval(equation) and equation not in done and eval(equation) >= 0 and eval(equation) <= 9:
        print(eval(equation), ' === ', equation)
        done.add(equation)
    
