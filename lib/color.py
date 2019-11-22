class Color:
    def __init__(self, txt):
        self.txt = txt
        self.codes = []
    
    def add_code(self, open_code, close_code = 39):
        self.codes.append({
            "open": "\x1b[{}m".format(open_code),
            "close": "\x1b[{}m".format(close_code)
        })
    
    def black(self, bg = False):
        code = 30
        if bg == True:
            self.add_code(code + 10, 49)
        else:
            self.add_code(code)
        return self

    def red(self, bg = False):
        code = 31
        if bg == True:
            self.add_code(code + 10, 49)
        else:
            self.add_code(code)
        return self
    
    def green(self, bg = False):
        code = 32
        if bg == True:
            self.add_code(code + 10, 49)
        else:
            self.add_code(code)
        return self

    def yellow(self, bg = False):
        code = 33
        if bg == True:
            self.add_code(code + 10, 49)
        else:
            self.add_code(code)
        return self

    def blue(self, bg = False):
        code = 34
        if bg == True:
            self.add_code(code + 10, 49)
        else:
            self.add_code(code)
        return self

    def magenta(self, bg = False):
        code = 35
        if bg == True:
            self.add_code(code + 10, 49)
        else:
            self.add_code(code)
        return self

    def cyan(self, bg = False):
        code = 36
        if bg == True:
            self.add_code(code + 10, 49)
        else:
            self.add_code(code)
        return self

    def white(self, bg = False):
        code = 37
        if bg == True:
            self.add_code(code + 10, 49)
        else:
            self.add_code(code)
        return self

    def gray(self):
        self.add_code(90)
        return self

    def bold(self):
        self.add_code(1, 22)
        return self
    
    def dim(self):
        self.add_code(2, 22)
        return self
    
    def italic(self):
        self.add_code(3, 23)
        return self

    def underline(self):
        self.add_code(4, 24)
        return self
    
    def strikethrough(self):
        self.add_code(9, 29)
        return self
    
    def render(self):
        open_codes = []
        close_codes = []
        for code in self.codes:
            open_codes.append(code["open"])
            close_codes.append(code["close"])
        return "{}{}{}".format("".join(open_codes), self.txt, "".join(close_codes))