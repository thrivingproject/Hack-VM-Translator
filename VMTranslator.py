import sys
from parser import Parser
from code_writer import CodeWriter
from command_type import CommandType

vm_path = sys.argv[1]
parser = Parser(vm_path)
cw = CodeWriter(vm_path)

while parser.has_more_lines():
    parser.advance()
    command = parser.command_type()
    match command:
        case CommandType.C_PUSH | CommandType.C_POP:
            segment = parser.arg_1()
            index = parser.arg_2()
            cw.write_push_pop(command, segment, index)
        case CommandType.C_ARITHMETIC:
            cw.write_arithmetic(parser.arg_1())
cw.close()
