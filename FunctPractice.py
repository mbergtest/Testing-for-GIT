def alphabetize(original_list=[]):
    """Pass any list in square brackets"""
    sorted_list = original_list.copy()
    sorted_list.sort()
    final_list = ''
    for name in sorted_list:
        final_list += name + ', '
    final_list = final_list[:-2]
    print(final_list)

names = ['Lee', 'Andy', 'Mike']
alphabetize(names)

#Added a line here to test versioning
#Added another line for test versioning