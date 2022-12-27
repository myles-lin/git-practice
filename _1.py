# 計算機 again & again [正確]

s = input().split()
operator_level = {'(': 0, '+': 1, '-':2, '*': 3, '/': 3, ')': 4}

for i in range(len(s)):
    try:
        if type(float(s[i])) == float:
            s[i] = float(s[i])
    except ValueError:
        pass

num = []
operator = []

tmp = 0
while (len(s) > 0 or len(operator) > 0):
    
    tag = 0
    if len(operator) > 1:
        tmp = operator_level[operator[-1]]
    else:
        tmp = 0
    
    while len(s) > 0:
        if tag == 1:
            break
        if type(s[0]) == float:
            num.append(s[0])
            s.pop(0)
        else:
            if operator_level[s[0]] >= tmp or s[0] == '(':
                operator.append(s[0])
                tmp = operator_level[s[0]]
                s.pop(0)
                if tmp == 4:
                    tag = 1
            elif operator_level[s[0]] < tmp and s[0] != '(':
                tag = 1
                
    right_brackets = 0
    while len(operator) > 0:
        
        LastOne = operator.pop(-1)
        if LastOne == ')':
            right_brackets = 1
        if LastOne == '(' and right_brackets == 1:
            break
        if LastOne == '(' and right_brackets == 0:
            operator.append(LastOne)
            break
        if LastOne == '+' and len(num) >= 2:
            b = num.pop(-1)
            a = num.pop(-1)
            num.append(a + b)
        if LastOne == '-' and len(num) >= 2:
            b = num.pop(-1)
            a = num.pop(-1)
            num.append(a - b)
        if LastOne == '*' and len(num) >= 2:
            b = num.pop(-1)
            a = num.pop(-1)
            num.append(a * b)
        if LastOne == '/' and len(num) >= 2:
            b = num.pop(-1)
            a = num.pop(-1)
            num.append(a / b)

print(num[0])
print(round(num[0], 4))