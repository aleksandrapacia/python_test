def get_formatted(first, last, middle=''): # optional arg middle
    if middle:
        full_name = f"{first} {middle} {last}"
    else: 
        full_name = f"{first} {last}"
    return full_name.title()