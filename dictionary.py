eggs = {'name': 'John', 'age': '12', 'species': 'human'}

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k, v in eggs.items():
	print(k, v)

print(eggs.get('color', 'red'))

eggs.setdefault('color', 'black')
eggs.setdefault('color', 'orange')
print(eggs['color'])