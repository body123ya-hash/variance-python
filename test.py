data = [1, 2, 3]

mdata = sum(data) / len(data)

sdata = [(x - mdata) for x in data]
edata = [x**2 for x in sdata]

ndata = sum(edata) / len(data)

print(ndata)