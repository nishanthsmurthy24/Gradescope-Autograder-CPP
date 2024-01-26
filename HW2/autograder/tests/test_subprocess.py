import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
from difflib import Differ

def compare_strings(string1, string2):
    differ = Differ()
    # lines1 = string1.splitlines()
    # lines2 = string2.splitlines()
    # diff = list(differ.compare([lines1[0]], [lines2[0]]))
    diff = list(differ.compare(string1.splitlines(), string2.splitlines()))
    return '\n'.join(diff)

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    # Associated point value within GradeScope
    @weight(0)
    def test00(self):
        #Title used by Gradescope 
        """HW2A - Compilation Test"""

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
    @weight(1)
    def test01(self):
        #Title used by Gradescope 
        """HW2A - Digit"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "1", "/autograder/source/reference/refA1.txt"]).decode('utf-8').strip()

        cat.kill()

        buffer = output.splitlines()
        out = buffer[0]

        result = compare_strings(out, reference)
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
    @weight(1)
    def test02(self):
        #Title used by Gradescope 
        """HW2A - Digit"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "1", "/autograder/source/reference/refA2.txt"]).decode('utf-8').strip()

        cat.kill()

        buffer = output.splitlines()
        out = buffer[0]

        result = compare_strings(out, reference)
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
    @weight(1)
    def test03(self):
        #Title used by Gradescope 
        """HW2A - Lower-Case Letter"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "1", "/autograder/source/reference/refA3.txt"]).decode('utf-8').strip()

        cat.kill()

        buffer = output.splitlines()
        out = buffer[0]

        result = compare_strings(out, reference)
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
    @weight(1)
    def test04(self):
        #Title used by Gradescope 
        """HW2A - Lower-Case Letter"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "1", "/autograder/source/reference/refA4.txt"]).decode('utf-8').strip()

        cat.kill()

        buffer = output.splitlines()
        out = buffer[0]

        result = compare_strings(out, reference)
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
    @weight(1)
    def test05(self):
        #Title used by Gradescope 
        """HW2A - Upper-Case Letter"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA5.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "1", "/autograder/source/reference/refA5.txt"]).decode('utf-8').strip()

        cat.kill()

        buffer = output.splitlines()
        out = buffer[0]

        result = compare_strings(out, reference)
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
    @weight(1)
    def test06(self):
        #Title used by Gradescope 
        """HW2A - Upper-Case Letter"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA6.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "1", "/autograder/source/reference/refA6.txt"]).decode('utf-8').strip()

        cat.kill()

        buffer = output.splitlines()
        out = buffer[0]

        result = compare_strings(out, reference)
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
    @weight(4)
    def test07(self):
        #Title used by Gradescope 
        """HW2A - Loop & Exit"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA7.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        ref = subprocess.Popen(["cat", "/autograder/source/reference/refA7.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        ref.kill()

        result = compare_strings(output, reference)
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
    def test08(self):
        #Title used by Gradescope 
        """HW2B - Compilation Test"""

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
    def test13(self):
        #Title used by Gradescope 
        """HW2C - Compilation Test"""

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