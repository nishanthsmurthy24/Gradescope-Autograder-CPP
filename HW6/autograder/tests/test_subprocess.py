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

def read_file_contents(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    # Associated point value within GradeScope
    @weight(0)
    def test00(self):
        #Title used by Gradescope 
        """HW6A - Compilation Test"""

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
    @weight(0)
    def test01(self):
        # Title used by Gradescope 
        """HW6A - Testcase 1"""

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/inA1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./HW6A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        print(f"Minimum Value: 1\nMaximum Value: 6\n\nYour Output\n\n{output}")

        cat.kill()

        num_lines = len(output.splitlines())

        # Standard unit test case with an associated error message
        if num_lines > 14:
            print("\nNumber of iterations exceeded (or) Check I/O Formatting!!")
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
    def test02(self):
        # Title used by Gradescope 
        """HW6A - Testcase 2"""

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/inA2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./HW6A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        print(f"Minimum Value: 1\nMaximum Value: 20\n\nYour Output\n\n{output}")

        cat.kill()

        num_lines = len(output.splitlines())

        # Standard unit test case with an associated error message
        if num_lines > 14:
            print("\nNumber of iterations exceeded (or) Check I/O Formatting!!")
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
    def test03(self):
        # Title used by Gradescope 
        """HW6A - Testcase 3"""

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/inA3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./HW6A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        print(f"Minimum Value: 4\nMaximum Value: 10\n\nYour Output\n\n{output}")

        cat.kill()

        num_lines = len(output.splitlines())

        # Standard unit test case with an associated error message
        if num_lines > 14:
            print("\nNumber of iterations exceeded (or) Check I/O Formatting!!")
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
    def test04(self):
        # Title used by Gradescope 
        """HW6A - I/O Formatting"""

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/inA4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./HW6A"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        print(f"Minimum Value: 3\nMaximum Value: 3\n")

        ref = subprocess.Popen(["cat", "/autograder/source/reference/refA4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        ref.kill()

        result = compare_strings(output, reference, 13)
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
        """HW6B - Compilation Test"""

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
    def test20(self):
        #Title used by Gradescope 
        """HW6C - Compilation Test - Optional"""

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