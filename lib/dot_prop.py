from copy import deepcopy

def __get_path_segments(path):
    path_arr = path.split(".")
    return path_arr

def __has_value(obj, key):
    try:
        obj[key]
        return True
    except KeyError:
        return False
    except TypeError:
        try:
            obj[int(key)]
            return True
        except IndexError:
            return False

def get(obj, path, value = None):
    if (not isinstance(obj, dict) and not isinstance(obj, list)) or not isinstance(path, str):
        return value if value is not None else obj
    
    path_arr = __get_path_segments(path)

    for i in range(len(path_arr)):
        if not __has_value(obj, path_arr[i]):
            return value
        
        obj = obj[int(path_arr[i])] if isinstance(obj, list) else obj[path_arr[i]]

        if obj is None:
            if i is not len(path_arr) - 1:
                return value

            break
    
    return obj

