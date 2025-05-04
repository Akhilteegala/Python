def halve_string(input_string):
    if len(input_string) % 2 == 0:
        mid = int(len(input_string)/2)
    else:
        a_mid = int(len(input_string)+1)
        mid = int(a_mid/2)
    a = input_string[:mid]
    b = input_string[mid:]
    return (a,b)
