def solution(s):
    if len(s)%2==1:
        return 0
    stack=[s[0]]
    i=1

    while i<len(s):
        while stack and stack[-1]==s[i]:
            stack.pop()
            i+=1
        if i<len(s):
            stack.append(s[i])
            i+=1

    return 0 if len(stack) else 1