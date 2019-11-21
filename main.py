key = list(input('type the first alphabet'))
unkey = list(input('type the second alphabet'))
encode1 = input('type information to encode')
encode2 = input('type information to decode')
decode1 = ''
decode2 = ''
diction = {}
for i in range(len(key)):
    diction.update({key.pop():unkey.pop()})
for i in encode1:
    decode1 += diction.get(i)
for i in encode2:
    decode2 += dict(map(reversed, diction.items())).get(i)
print(decode1)
print(decode2)
