import base64
import re

def is_not_empty (var):
    if (isinstance(var, bool)):
        return var
    elif (isinstance(var, int)):
        return not var == 0
    elif (isinstance(var, list)):
        return len(var) > 0
    empty_chars = ["", "null", "nil", "false", "none"]
    return var is not None and not any(c == "{}".format(var).lower() for c in empty_chars)

def is_true (var):
    if (isinstance(var, bool)):
        return var
    false_char = ["false", "ko", "no", "off"]
    return is_not_empty(var) and not any(c == "{}".format(var).lower() for c in false_char)

def is_false (var):
    return not is_true(var)

def is_empty (var):
    return not is_not_empty(var)

def is_empty_key(vdict, key):
    return is_empty(vdict) or not key in vdict or is_empty(vdict[key])

def is_not_empty_key(vdict, key):
    return not is_empty_key(vdict, key)

def remove_key_safely(vdict, key):
    if is_not_empty_key(vdict, key):
        del vdict[key]

def get_or_else(vdict, key, default):
    return default if is_empty_key(vdict, key) else vdict[key]

def is_numeric (var):
    if (isinstance(var, int)):
        return True
    return is_not_empty(var) and str(var).isnumeric()

def is_not_numeric (var):
    return not is_numeric(var)

def is_disabled (var):
    return is_empty(var) or "changeit" in var

def is_enabled(var):
    return not is_disabled(var)

def exists_entry(dictionary, key):
    return key in dictionary and is_not_empty(dictionary[key])

def safe_compare_entry(dictionary, key, expected_value):
    return exists_entry(dictionary, key) and is_not_empty(expected_value) and dictionary[key] == expected_value

def safe_contain_entry(dictionary, key, expected_contained_value):
    return exists_entry(dictionary, key) and is_not_empty(expected_contained_value) and expected_contained_value in dictionary[key]

def safe_get_entry_with_default(dictionary, key, default_value):
    return default_value if not exists_entry(dictionary, key) else dictionary[key]

def safe_get_entry(dictionary, key):
    return safe_get_entry_with_default(dictionary = dictionary, key = key, default_value = None)

def name_from_email(email):
    first_part = email.split("@")[0]
    infos = first_part.split(".")
    return {
        "first_name": infos[0] if len(infos) > 0 and is_not_empty(infos[0]) else "X.",
        "last_name": infos[1] if len(infos) > 1 and is_not_empty(infos[1]) else "X."
    }

def is_response_ok(code):
    return code >= 200 and code < 400

def is_duration_valid(duration):
    return is_not_empty(duration) and duration != -1

def unbase64(encoded_data):
    decoded_content = base64.b64decode(encoded_data)
    return decoded_content.decode('utf-8')

def is_uuid (var):
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89a-bA-B][0-9a-f]{3}-[0-9a-f]{12}$'
    return bool(re.match(pattern, var))

def is_not_uuid (var):
    return not is_uuid(var)
