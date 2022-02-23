import softest


class Utils (softest.TestCase):
    def assertItemText(self, var_name, value):
        print("The text is " + var_name.text)
        # Using the the softest (soft assertion class in this site: https://pypi.org/project/softest/
        # assert var_name.text != value
        self.soft_assert(self.assertNotEqual, var_name.text, value)
        # create a simple if else statement
        if var_name.text != value:
            print("test passed")
        else:
            print("test failed")
        # Since we need to continue the verification even if there is an assertion in the middle.
        self.assert_all()