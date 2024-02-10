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
        """HW3A - Compilation Test"""

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["make", "a"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
    @weight(2.5)
    def test01(self):
        #Title used by Gradescope 
        """HW3A - Positive Integer"""

        cat = subprocess.Popen(["cat", "/autograder/source/input/inA1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            test = subprocess.run(["./HW3A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "4", "/autograder/source/reference/refA1.txt"]).decode('utf-8').strip()

        cat.kill()

        print(f"Input: 4\n")

        result = compare_strings(output, reference, 4)
        print(result)

        # Standard unit test case with an associated error message
        if reference in output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")
        
        cat.terminate()

    # Associated point value within GradeScope
    @weight(2.5)
    def test02(self):
        #Title used by Gradescope 
        """HW3A - Negative Integer"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW3A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "7", "/autograder/source/reference/refA2.txt"]).decode('utf-8').strip()

        cat.kill()

        print(f"Input: -7\n")

        result = compare_strings(output, reference, 7)
        print(result)

        # Standard unit test case with an associated error message
        if reference in output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")
        
        cat.terminate()

    # Associated point value within GradeScope
    @weight(5)
    def test03(self):
        #Title used by Gradescope 
        """HW3A - Loop Condition"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW3A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "25", "/autograder/source/reference/refA3.txt"]).decode('utf-8').strip()

        cat.kill()

        print(f"Input Sequence: -12, 5, -8\n")

        result = compare_strings(output, reference, 25)
        print(result)

        # Standard unit test case with an associated error message
        if reference in output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")
        
        cat.terminate()

    # Associated point value within GradeScope
    @weight(2)
    def test04(self):
        #Title used by Gradescope 
        """HW3A - Invalid Input & Exit"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW3A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        ref = subprocess.Popen(["cat", "/autograder/source/reference/refA4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        ref.kill()

        print(f"Input Sequence: -85, 51, 0\n")

        result = compare_strings(output, reference, 3)
        print(result)

        # Standard unit test case with an associated error message
        if reference in output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()
        ref.terminate()
    
    # Associated point value within GradeScope
    @weight(0)
    def test05(self):
        #Title used by Gradescope 
        """HW3B - Compilation Test"""

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["make", "b"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
    @weight(0)
    def test06(self):
        #Title used by Gradescope 
        """HW3B - Testcase - 1"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW3B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!!"

        print(f"Initial Vaue: 255\nNo. of Iterations: 10\nUpdate Size: ±10\n\nYour Output\n\n{output}")

        num_lines = len(output.splitlines())

        # Standard unit test case with an associated error message
        if num_lines > 11:
            print("\nNumber of iterations exceeded!!")
            self.assertTrue(False, msg="")
        if output != "Timeout expired!!":
            print("\nProgram Exit Succesfully!!")
            self.assertTrue(True, msg="")
        else:
            print("\nProgram did not Exit Successfully!!")
            self.assertTrue(False, msg="")

        cat.terminate()
    
    # Associated point value within GradeScope
    @weight(0)
    def test07(self):
        #Title used by Gradescope 
        """HW3B - Testcase - 2"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW3B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!!"

        print(f"Initial Vaue: 0\nNo. of Iterations: 20\nUpdate Size: ±2\n\nYour Output\n\n{output}")

        num_lines = len(output.splitlines())

        # Standard unit test case with an associated error message
        if num_lines > 21:
            print("\nNumber of iterations exceeded!!")
            self.assertTrue(False, msg="")
        if output != "Timeout expired!!":
            print("\nProgram Exit Succesfully!!")
            self.assertTrue(True, msg="")
        else:
            print("\nProgram did not Exit Successfully!!")
            self.assertTrue(False, msg="")

        cat.terminate()
    
    # Associated point value within GradeScope
    @weight(2)
    def test08(self):
        #Title used by Gradescope 
        """HW3B - Invalid Input"""

        cat = subprocess.Popen(["cat", "/autograder/source/input/inB3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            test = subprocess.run(["./HW3B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "4", "/autograder/source/reference/refB3.txt"]).decode('utf-8').strip()

        cat.kill()

        print(f"Input Sequence: 260, 256, -9\n")

        result = compare_strings(output, reference, 4)
        print(result)

        # Standard unit test case with an associated error message
        if reference in output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")
        
        cat.terminate()
    
    # Associated point value within GradeScope
    @weight(2)
    def test09(self):
        #Title used by Gradescope 
        """HW3B - I/O Formatting"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW3B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        ref.kill()

        print(f"Initial Vaue: 200\nNo. of Iterations: 10\nUpdate Size: 0\n")

        result = compare_strings(output, reference, 10)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")

        cat.terminate()
        ref.terminate()

    # Associated point value within GradeScope
    @weight(0)
    def test10(self):
        #Title used by Gradescope 
        """HW3C - Compilation Test"""

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["make", "c"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
    @weight(0)
    def test11(self):
        #Title used by Gradescope 
        """HW3C - Output"""

        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW3C"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!!"

        print(f"Your Output\n\n{output}")

        num_lines = len(output.splitlines())

        # Standard unit test case with an associated error message
        if num_lines > 29:
            print("\nToo many Lines in output!!")
            self.assertTrue(False, msg="")
        if output != "Timeout expired!!":
            print("\nProgram Exit Succesfully!!")
            self.assertTrue(True, msg="")
        else:
            print("\nProgram did not Exit Successfully!!")
            self.assertTrue(False, msg="")
