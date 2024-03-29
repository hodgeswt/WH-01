'''
	Assembler for WH-01 Processor
	Opcodes are defined below

	Other operands:
		# a v // stores value v at address a
		: xxx // Does a comment. 
		O a   // Starts code at the provided address
	Comments are valid at the end of any completed line
		or at the start of a line, if preceded by ;
'''

import sys
import re

input_file = sys.argv[1]
size = int(sys.argv[2])
output_file = sys.argv[3]

opcodes = {
	'NOP' : 0b0000, # No operation
	'LDA' : 0b0001, # Load A register with value store at memory address operand
	'ROT' : 0b0010, # Output the value at the current ram address to the display
	'AOT' : 0b0011, # Output the value of the A register to the display
	'JMP' : 0b0100, # Jump operation to line indicated by operand
	'HLT' : 0b0101, # Halt execution
	'ADA' : 0b0110, # Add value stored at memory address operand to the A register
	'SBA' : 0b0111, # Subtract value stored at mem addrs operand to the A register
	'STA' : 0b1000, # Store value of A register to provided memory address
	'LDB' : 0b1001, # Load B register with value stored at memory address operand
 	'BOT' : 0b1010, # Output value at B register to display
 	'LDC' : 0b1011, # Add value at ram address to B register - Overwrites A register
 	'COT' : 0b1100, # Subtract value at ram address from B register - Overwrites A register
 	'STB' : 0b1101, # Store B at indicated memory address
	'BEQ' : 0b1110, # Jumps to provided memory address if the equal flag is set
	'BNE' : 0b1111, # Jumps to provided memory address if the equal flag was not set
	'UFR' : 0b10000,# Latches outputs from ALU to the flags register
	'BZO' : 0b10001,# Branches if the ALU output == 0
	'PHA' : 0b10010,# Pushes A value onto stack
	'PLA' : 0b10011,# Pulls A value off of stack
	'JST' : 0b10100,# Jumps to provided address and stores current address on stack
	'RST' : 0b10101,# Jumps to value on stack. Pass 00 as argument
	'BTA' : 0b10110,# Move B register to A register
 	'CTA' : 0b10111,# Move C register to A register
 	'ATB' : 0b11000,# Move A register to B register
 	'ATC' : 0b11001,# Move A register to C register
	'LT'  : 0b11010,# Loads value at given address into TMP register
	'ATO' : 0b11011,# Outputs A to Output Register 2
 	'BTO' : 0b11100,# Outputs B to Output Register 2
	'ADI' : 0b11101,# Address Register in
	'ATX' : 0b11111,# Outputs A to Serial Out
	'ARI' : 0b100000, # Address register increment
	'ARD' : 0b100001, # Address register decrement
	'AIA' : 0b100010, # Stores value at address register into A register
	'RIR' : 0b100011, # Reads value from Input Register into A register
	'SAR' : 0b100100, # Stores address register
	'TAD' : 0b100101  # Stores A register at address in address register
}

code = ['{0:0{1}X}'.format(0b0,6) for i in range(size)]
s = "v2.0 raw\n"

f = open(input_file, 'r')
add = 0
var = {}
pointers = {}
for line in f:
	if (line[0] == ';'): # Ignore comments
		pass			 # Comments at ends of lines shoul
						 # be ignored by default

	elif (line[0] == ':'): # Store value at proper address
		add += int(line.split()[1], 16)
	elif (line[0] == '&'):
		if (line.split()[1][0] == "_"):
			a = pointers[line.split()[1]]
		else:
			a = line.split()[1]
		a = int(a,16)
		l = re.findall(r'"(.*?)"',line)[0]
		for i in range(0, len(l)):
			code[a] = hex(ord(l[i]))[2:].rjust(6,'0')
			a -= 1
	elif (line[0] == "."):
		v = line[1:-1]
		var[v] = add
	elif (line[0] == "_"):
		pointers[line.split()[0]] = line.split()[1]
	else:
		op = line.split()[0]
		if (op == "#"): # If setting a memory value
			a = line.split()[1] # address
			if (a[0] == "_"):
				a = pointers[a]
			v = line.split()[2] # value
			if (v[0] != '%'):
				code[int(a, 16)] = v.rjust(6,'0') # process add as hex, make val 4 digits
			else:
				if (len(v) > 2):
					raise ValueError("Character on line " + add + "must be one character")
				elif (len(v) == 2):
					code[int(a, 16)] = hex(ord(v[1:]))[2:].rjust(6,'0')
				else:
					code[int(a, 16)] = '000020' # space
		else:
			op = opcodes[op]
			op = op << 16

			opd = line.split()[1]
			if (opd[0] == "."):
				try:
					opd = var[opd[1:]]
				except:
					raise Exception("Variable not yet declared")
			elif (opd[0] == "_"):
				try:
					opd = int(pointers[opd],16)
				except:
					raise Exception("Variable not yet declared")
			else:
				opd = int(opd, 16)

			word = bin(op ^ opd)
			word = word[2:]
			word = hex(int(word,2))
			word = word[2:].rjust(6,'0')
			code[add] = word
			add += 1
f.close()

empty_line = "000000 000000 000000 000000 000000 000000 000000 000000 000000 000000 000000 000000 000000 000000 000000 000000"

c = 0
for w in code:
	if (c == 15):
		s += w + "\n"
		c = 0
	else:
		s += w + " "
		c += 1
last_output = ""
for line in s.splitlines():
	if line != empty_line:
		if (last_output == "."):
			print()
			print(line)
			last_output = ""
		else:
			print(line)
			last_output = ""
	else:
		last_output = "."
		print(".", end="")

f = open(output_file, 'w')
f.write(s)
f.close()
