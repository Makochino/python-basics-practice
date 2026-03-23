def rdl_by_k(s):
    k = 3
    stack = []
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])

    result = ''
    for char, count in stack:
        result += char * count
    return result

print(rdl_by_k("deeeceeeccc"))