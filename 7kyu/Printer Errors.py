def printer_error(s):
    counts = len(s)
    error = 0
    for i in s:
        if i >= 'a' and i <= 'm':
            pass
        else: 
            error += 1
    return f'{error}/{counts}'
