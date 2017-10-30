limit = 1000 + 1
for a in range(1, limit): # if 0 is allowed trivial answer a,b,c=0,500,500
    answerFound = False
    for b in range(a + 1, limit - a):
        c = 1000 - b - a
        if a ** 2 + b ** 2 != c ** 2:
            continue
        else:
            print("a, b, c: ", a, b, c)
            print("abc = ", a * b * c)
            answerFound = True
            break
    if answerFound:
        break
