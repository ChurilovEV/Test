def count(s):
    def pos(cc, ss):  # позиция в строке где указана операция +-*/
        var = 0
        ll = len(cc)
        while var < ll:
            pp = ss.find(cc[var])
            if pp > 0: break
            var += 1
        return pp

    c = ['-', '+', '/', '*', '%']
    p = pos(c, s)
    op = s[p]
    sp = s.split(op)
    if   op == c[0]: rez = int(sp[0]) - int(sp[1])
    elif op == c[1]: rez = int(sp[0]) + int(sp[1])
    elif op == c[2]: rez = int(sp[0]) / int(sp[1])
    elif op == c[3]: rez = int(sp[0]) * int(sp[1])
    else: rez = int(sp[0]) / 100
    return rez
print(count('1+9'))
print(count('11-5'))
print(count('3*4'))
print(count('12/3'))
print(count('100%'))
