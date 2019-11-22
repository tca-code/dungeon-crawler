import os
from copy import deepcopy
from lib.get_console_width import get_console_width

def __get_lines(txt, console_width):
    words = txt.split(" ")
    max_line_len = console_width - 4
    
    current_word_idx = 0
    lines = [""]

    while True:
        current_line = lines[len(lines) - 1]
        current_word = words[current_word_idx]

        if len(current_line) + len(current_word) + 1 < max_line_len:
            lines[len(lines) - 1] = current_line + " " + current_word
        else:
            lines.append(current_word)
        
        if current_word_idx is len(words) - 1:
            break
        
        current_word_idx += 1
    
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    return lines

def __pad(amount):
    string = ""
    for i in range(amount):
        string += " " 
    return string

def __pad_lines(lines, console_width):
    max_line_len = console_width - 4
    new_lines = deepcopy(lines)

    for i in range(len(lines)):
        current_line = lines[i]
        padding_len = max_line_len - len(current_line)
        new_lines[i] = "| {}{} |".format(current_line, __pad(padding_len))
    
    return new_lines

def __get_line(console_width, footer = False):
    string = " " if not footer else "|"
    for i in range(console_width - 2):
        string += "_"
    return string if not footer else "{}|".format(string)

def message(txt):
    console_width = get_console_width()
    max_line_len = 45 if console_width >= 45 else console_width
    lines = __get_lines(txt, max_line_len)
    padded_lines = __pad_lines(lines, max_line_len)
    
    box_top = [__get_line(max_line_len)]
    box_bottom = [__get_line(max_line_len, True)]
    empty_line = __pad_lines([__pad(max_line_len - 4)], max_line_len)

    message_box = box_top + empty_line + padded_lines + box_bottom
    return "\n".join(message_box)
