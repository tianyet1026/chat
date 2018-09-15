#展示清單分割法
lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
print(lines)

for line in lines:
	s = line.split(' ')
	name = s[0][5:]
	time = s[0][:5]
	print(name)
	print(time)