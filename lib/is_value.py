def number(val):
    try:
        int(val)
        return True
    except ValueError:
        return False