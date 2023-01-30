
# A function takes a string and shrinks it to 16 characters 
# if a string is longer than 16 characters -> show first 13 , and add three dots 
# If a string is shorter than 16 characters -> fill the extra space with whitespaces

def transform_string(title):
    if len(title) < 16:
        new_title = title + ' ' * (16 - len(title))
        print(len(new_title))
        return new_title
    elif len(title) > 16:
        new_title = title[:13] + '.' * 3 
        print(len(new_title))
        return new_title
