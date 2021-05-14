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
#Added another line to test add and commit 5/10
#Modified code again 5/10

#Added a comment at the end of the branched version, then merged to master
#Added another comment at the end of the branched version
#Added a different line 21 to branch1 version
#Added a line 21 here in Master branch
#Added line 23 in remote master.

#Adding line 25 comment 5/14.