import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
from difflib import Differ

def compare_strings(string1, string2, n):
    differ = Differ()
    lines1 = string1.splitlines()[:n]
    lines2 = string2.splitlines()[:n]
    diff = list(differ.compare(lines1, lines2))
    # diff = list(differ.compare(string1.splitlines(), string2.splitlines()))
    return '\n'.join(diff)


class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    # Associated point value within GradeScope
    @weight(0)
    def test00(self):
        #Title used by Gradescope 
        """Compilation Test"""

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stderr.read().strip().decode('utf-8')
        test.kill()

        # Standard unit test case with an associated error message
        if "error" in output:
            print("COMPILATION FAILED!!")
            self.assertTrue( output == "", msg=output)
        elif "Stop" in output:
            print("COMPILATION FAILED!!")
            self.assertTrue( output == "", msg=output)
        else:
            print("COMPILATION SUCCESSFUL!!")
        
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(1)
    def test01(self):
        # Title used by Gradescope 
        """HW7 - Testcase 1"""

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/in1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./HW7"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["tail", "-n", "1", "/autograder/source/reference/ref1.txt"]).decode('utf-8').strip()

        cat.kill()

        print(f"(3) + (2)x^1 + (1)x^2")
        print(f"times")
        print(f"(2) + (2)x^1 + (2)x^2")

        # Compare the contents
        print(f"\nExpected Output:\n{reference}\n")
        print(f"Your Output:\n{output.splitlines()[-1]}")

        # Standard unit test case with an associated error message
        if reference in output.splitlines()[-1]:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test02(self):
        # Title used by Gradescope 
        """HW7 - Testcase 2"""

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/in2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./HW7"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["tail", "-n", "1", "/autograder/source/reference/ref2.txt"]).decode('utf-8').strip()

        cat.kill()

        print(f"(1) + (-2)x^1 + (3)x^2")
        print(f"times")
        print(f"(3) + (-2)x^1 + (-1)x^2")

        # Compare the contents
        print(f"\nExpected Output:\n{reference}\n")
        print(f"Your Output:\n{output.splitlines()[-1]}")

        # Standard unit test case with an associated error message
        if reference in output.splitlines()[-1]:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test03(self):
        # Title used by Gradescope 
        """HW7 - Testcase 3"""

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/in3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./HW7"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["tail", "-n", "1", "/autograder/source/reference/ref3.txt"]).decode('utf-8').strip()

        cat.kill()

        print(f"(-1) + (2)x^1")
        print(f"times")
        print(f"(1) + (3)x^1 + (-4)x^2")

        # Compare the contents
        print(f"\nExpected Output:\n{reference}\n")
        print(f"Your Output:\n{output.splitlines()[-1]}")

        # Standard unit test case with an associated error message
        if reference in output.splitlines()[-1]:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test04(self):
        # Title used by Gradescope 
        """HW7 - Testcase 4"""

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/in4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./HW7"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["tail", "-n", "1", "/autograder/source/reference/ref4.txt"]).decode('utf-8').strip()

        cat.kill()

        print(f"(2)")
        print(f"times")
        print(f"(5) + (-4)x^1 + (0)x^2 + (-2)x^3 + (1)x^4")

        # Compare the contents
        print(f"\nExpected Output:\n{reference}\n")
        print(f"Your Output:\n{output.splitlines()[-1]}")

        # Standard unit test case with an associated error message
        if reference in output.splitlines()[-1]:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()