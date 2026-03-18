#-----title case----------


def format_name (f_name, l_name, g_name):
    """Take a first, last and grand pa  name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "" or g_name == "":
        return "you didin't provide all valid inputs"
    
    foramated_f_name = f_name.title()
    foramted_l_name = l_name.title()
    foramted_g_name = g_name.title()
    return f"{foramated_f_name} {foramted_l_name} {foramted_g_name}"
    



print(format_name(input("What is your name? "), input("What is your father's name "), input("What about your grand pa? ")))
