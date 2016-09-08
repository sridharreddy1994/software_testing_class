# parser.py

def parse(s):
    if '.' in s:
        (si, sd) = s.split('.')
    else:
        (si, sd) = (s,"")
    n = 0
    for c in si:
        n = n * 10 + int(c)
    d = 0.1
    for c in sd:
        n = n + (int(c) * d)
        d = d / 10.0
    return n
    
    
