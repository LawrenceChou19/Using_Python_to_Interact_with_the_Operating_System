#!/usr/bin/env python3

def character_frequency(filename):
    """Counts the frequency of each character in the given file."""
    try:
        f = open(filename)
    except OSError:
        return None
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char,0)+1
    f.close()
    return characters

# print(validate_user2([3],1))
import unittest
from validations import validate_user


class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser",3),True)
    
    def test_too_short(self):
        self.assertEqual(validate_user("inv",5),False)
    
    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user",1),False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError,validate_user,"user",-1)

unittest.main()
