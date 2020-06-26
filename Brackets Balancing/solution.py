'''
Author: Ashutosh Srivastava
Python3 solution
'''
#Solution 1:-

def solution(data, n):
    for i in data:
        num=data.count(i)
        if(num>n):
            data=list(filter(lambda x: x != i, data))
    return(data)

open_bracs=['{','[','(']
close_bracs=['}',']',')']
def validate(expression):
    stack=[]
    for i in expression:
        if i in open_bracs:
            stack.append(i)
        else:
            position=close_bracs.index(i)
            if(len(stack)>0 and open_bracs[position]==stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
    if(len(stack)==0):
        return "Balanced"
    else:
        return "Unbalanced"
N=input()
print("The Expression entered by you is ",validate(N))
    
#Solution 2:-
#only works if the expression contains digits 0-9, +, -, /, * and () brakets only

open_bracs=['{','[','(']
close_bracs=['}',']',')']
def validate(expression):
    stack=[]
    for i in expression:
        if i in open_bracs:
            stack.append(i)
        elif i in close_bracs:            
            position=close_bracs.index(i)
            if(len(stack)>0 and open_bracs[position]==stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
        elif i in ['1','2','3','4','5','6','7','8','9','0','+','*','/','-']:
            continue
        else:
            return "Invalid expression"
    if(len(stack)==0):
        try:
            res=eval(expression[0:len(expression)])
            return "Balanced"
        except:
            print("invalid",expression[0:len(expression)])
            return "Invalid Expression"
    else:
        return "Unbalanced"
N=input()
print("The Expression entered by you is",validate(N))
