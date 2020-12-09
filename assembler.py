import sys

input_file = sys.argv[1]

opcodes = {
	'NOP' : 0b0000, # No operation
	'LDA' : 0b0001, # Load A register with value store at memory address operand
	'ROT' : 0b0010, # Output the value at the current ram address to the display
	'AOT' : 0b0011, # Output the value of the A register to the display
	'JMP' : 0b0100, # Jump operation to line indicated by operand
	'HLT' : 0b0101, # Halt execution
	'ADA' : 0b0110, # Add value stored at memory address operand to the A register
	'SBA' : 0b0111  # Subtract value stored at mem addrs operand to the A register
}

code = ['{0:0{1}X}'.format(0b0,4)] * 16
s = "v2.0 raw\n"

f = open(input_file, 'r')
add = 0
for line in f:
	op = line.split()[0]
	opd = line.split()[1]
	op = opcodes[op]
	word = '{0:0{1}X}'.format((op << 4) ^ int(opd,16), 4)
	code[add] = word
	add += 1
f.close()

for w in code:
	s += w + " "	

print(s)
f = open('out.bin', 'w')
f.write(s)
f.close()
