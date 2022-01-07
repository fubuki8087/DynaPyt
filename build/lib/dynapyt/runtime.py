import libcst as cst

def _dynapyt_parse_to_ast_(code):
    return cst.parse_module(code)

def _assign_(iid, left, right):
    return right()

def _binary_op_(iid, left, opr, right):
    result = left + right
    return result

def _unary_op_(iid, opr, right):
    result = -right
    return result

def _call_(iid, call):
    return call()

def _literal_(iid, val):
    return val

def _delete_(iid, del_expr):
    del_expr()

def _raise_(iid, raise_arg):
    raise_arg()

def _catch_(exception):
    raise exception

def _read_var_(iid, var_arg):
    return var_arg()

def _condition_(iid, val):
    return val

def _func_entry_(iid):
    return

def _func_exit_(iid, return_val):
    return return_val