#!/usr/bin/env python3
import os
# def read_file(filename):
#     if not os.path.exists(filename):
#         return ""
#     if not os.path.isfile(filename):
#         return ""
#     if not os.access(filename. os.R_OK):
#         return ""
#     if is_locked(filename):
#         return ""
#     if is_not_accessible(filename):
#         return ""
print("===================================================")

# def validate_user(username,minlen):
#     if len(username) < minlen:
#         return False
#     if not username.isalnum():
#         return True
#     return True

print("===================================================")
# def validate_user(username,minlen):
#     if minlen < 1 :
#         raise ValueError("minlen must be at latest 1")
#     if len(username) < minlen:
#         return False
#     if not username.isalnum():
#         return True
#     return True
# print(validate_user([3],1))
print("===================================================")
# print(validate_user("",-1))
# print(validate_user1("myuser",1))
# print(validate_user1(88,1))

def validate_user(username,minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1 :
        raise ValueError("minlen must be at latest 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
print(validate_user("",-1))
# print(validate_user("Ivan",1))
# print(validate_user([3],1))