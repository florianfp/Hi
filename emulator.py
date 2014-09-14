# Tryo Bytes
# CEE 290I
# dlx emulator

## Initialize program ##

pc = 0
ir = []
register = []  # see if you can pre-determine the size
memory = []  # same as above 

''' sample_command = ADD 1,2,3'''

# figure out how to get from the text file to here

def parse_command(command):
    '''This function takes in a command in the form of a string from a text file.
    output is four parameters:
        op, A, B, and C'''
    op=''
    A=''
    B=''
    C=''
    for n in range(len(command)):
        if n<3:
            op = op + command[n]
        if n == 4:
            A = command[n]
        if n == 6:
            B = command[n]
        if n == 8:
            C = command[n]
    ir = [op, A, B, C] #ir stands for Instruction Register 
    return ir


##result = parse_command(command)         
##print result

##def execute_command(operation):
##    
def read_text_file():
    text_file = open('TEST.txt', 'r')
    commands = text_file.readlines()
    print ' this is commands ', commands
    instructions = []
    for command in commands:
        ir = parse_command(command)
        instructions += [ir] 
    return instructions

print read_text_file()
