import sys
from parser import Parser
from code_writer import CodeWriter
from command_type import CommandType

vm_path = sys.argv[1]
parser = Parser(vm_path)
code_writer = CodeWriter(vm_path)

while parser.has_more_lines():
    parser.advance()
    command = parser.command_type()
    match command:
        case CommandType.C_PUSH | CommandType.C_POP:
            code_writer.write_push_pop(command, parser.arg_1(), parser.arg_2())
        case CommandType.C_ARITHMETIC:
            code_writer.write_arithmetic(parser.arg_1())
code_writer.close()
