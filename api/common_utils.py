def is_not_empty (var):
    if (isinstance(var, bool)):
        return var
    elif (isinstance(var, int)):
        return False
    empty_chars = ["", "null", "nil", "false", "none"]
    return var is not None and not any(c == "{}".format(var).lower() for c in empty_chars)

def is_empty (var):
    return not is_not_empty(var)

def is_true (var) :
    false_char = ["false", "ko", "no", "disable", "disabled"]
    return is_empty(var) or not any(c == "{}".format(var).lower() for c in false_char)
