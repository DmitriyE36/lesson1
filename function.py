def get_summ(one, two, delimiter='&'):
    one = one.upper()
    two = two.upper()
    return f'{one} {delimiter} {two}'
    
a = get_summ('Learn', 'python')
print(a)