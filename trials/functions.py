def modify_string(string):
    string ="This text has been modified"
    return string
test_string="This is original text"
modify_string(test_string)
print(test_string)
test_string=modify_string(test_string)
print(test_string)