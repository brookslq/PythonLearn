#测试代码

def get_formatted_name(first,last, middle=" "):
    """Generate a neatly formatted full name"""
    full_name = first + middle + last
    return full_name.title()

# print("Enter 'q' at any time to quit.")
# while True:
#     first_name = input("\nPlease give me a first name: ")
#     if first_name == 'q':
#         break
#     last_name = input("\nPlease give me a last name: ")
#     if last_name == "q":
#         break
#
#     formatted_name = get_formatted_name(first_name, last_name)
#     print('\tNeatly formatted name: ' + formatted_name + '.')


