
n = int(input("introduce numero"))
h = ''
while n <= 60:
    if n%2 == 0:
        h += ' %i' % n
    n += 1
print h
