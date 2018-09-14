#整理對話紀錄
def read_file(filename):
	#with open('products.csv', 'r', encoding = 'utf-8-sig') as f:-sig是在開頭出現怪符號時使用
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			#if '郭建麟' in line:
			#	continue
			#print(chat)
			#if '駱潤生' in line:
			#	continue
			lines.append(line.strip())
	return lines
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == '郭建麟' :
			person = '郭建麟'
			continue
		elif line == '駱潤生':
			person = '駱潤生'
			continue
		elif person:
			new.append(person+ ': ' +line )
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()