from sys import stdout

# Keywords
KW_print        = 'ijustwannatelluhowimfeeling'
KW_if           = 'andifuaskmehowimfeeling'

KW_let          = 'give'
KW_assign       = 'up'
KW_import1      = 'weknowthe'
KW_import2      = "andwe'regonnaplayit"
KW_def1         = 'neverknew'
KW_def2         = 'couldfeelthisway'
KW_return1      = 'whenigivemy'
KW_return2      = 'itwillbecompletely'
KW_main         = 'takemetourheart'
KW_end          = 'saygoodbye'

KW_break        = 'desertu'
KW_continue     = 'runaround'
KW_endless_loop = 'togetherforeverandnevertopart'
KW_while_loop   = 'togetherforeverwith'

KW_less_than_OP = 'islessthan'
KW_greater_than_OP = 'isgreaterthan'
KW_is_not_OP = 'isnot'
KW_equals_OP = 'is'

keywords = [
    KW_print,
    KW_if,
    KW_let,
    KW_assign,
    KW_import1,
    KW_import2,
    KW_def1,
    KW_def2,
    KW_return1,
    KW_return2,
    KW_main,
    KW_end,
    KW_break,
    KW_continue,
    KW_endless_loop,
    KW_while_loop,
    KW_less_than_OP,
    KW_greater_than_OP,
    KW_is_not_OP,
    KW_equals_OP
]

all_keyword_string = ''
for i in keywords:
    all_keyword_string += i

# Tokens that the interpreter will totally ignore
ignore_tokens = {'~', "'"}

# Characters in numbers
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}

# Separators are used in tokenization
separators = {
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

# Operators
operators = {'+', '-', '*', '/', '%', '^', '=', '[', ']', '(', ')', '{', '}', ','}

OP_build_in_functions = {'to_string', 'to_int', 'to_float', 'length'}

def join_list(l):
    result = ''
    for i in l: result += f'{i}'
    return result
