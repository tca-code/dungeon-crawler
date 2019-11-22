def get_csv_contents(filepath):
    f = open(filepath, "r")
    contents = f.read().split("\n")
    f.close()
    return contents