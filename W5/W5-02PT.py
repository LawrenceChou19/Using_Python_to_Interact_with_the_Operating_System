# From the output, you can see that the LetterCompiler( ) function finds all matches for the letters a through c in an input string if followed by another character and returns them as a list of strings, with each string representing one match. Nice.

# But can we be sure that this function will always do what we expect it to do? We need to write code to help us catch mistakes, errors and bugs. 
# This code should automate the process of checking if the returned value of our code matches the expectations by dynamically feeding into it test cases. 
# Since we're dynamically feeding in different strings, it would be prudent to create unit tests for our code. We can use the module unittest for this.
# Fill in the blanks below to create an automatic unit test that verifies whether input strings have the correct list of string matches.
from LetterC import LetterCompiler
import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)# self.assertEqual(LetterCompiler(___), ___)

unittest.main()
# unittest.main(argv = ['first-arg-is-ignored'], exit = False) this using in the Jupyter
class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
unittest.main()
unittest.main(argv = ['first-arg-is-ignored'], exit = False)