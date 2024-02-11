def valid_parantheses(s):
    stack=[]
    mapping={')':'(','}':'{',']':'['}
    for i in s:
        if i in mapping.values():
            stack.append(i)
        elif i in mapping.keys():
            if not stack or stack.pop()!=mapping[i]:
                return False
        else:
            return False
    return not stack
p=input("enter the parantheses: ")
if valid_parantheses(p):
    print("entered parantheses is valid: ")
else:
    print("not")