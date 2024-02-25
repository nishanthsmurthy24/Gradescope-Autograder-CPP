import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
from difflib import Differ
import os

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
        """HW5A - Compilation Test"""

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
        #Title used by Gradescope 
        """HW5B - Compilation Test"""

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
    @weight(1)
    def test02(self):
        #Title used by Gradescope 
        """HW5B - Invalid Input & Exit"""

        print(f"Running program\n\n$ ./HW5B\n")
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW5B"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        ref.kill()

        result = compare_strings(output, reference, 3)
        print(result)

        # Standard unit test case with an associated error message
        if reference[:-2] in output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        ref.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test03(self):
        #Title used by Gradescope 
        """HW5B - Invalid Input & Exit"""
        
        print(f"Running program\n\n$ ./HW5B 4 4\n")

        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW5B", "4", "4"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        ref.kill()

        result = compare_strings(output, reference, 3)
        print(result)

        # Standard unit test case with an associated error message
        if reference[:-1] in output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        ref.terminate()
    
    # Associated point value within GradeScope
    @weight(1)
    def test04(self):
        # Title used by Gradescope 
        """HW5B - Output File - 'randArray.txt' """

        print(f"Running program\n\n$ ./HW5B 3 2 0\n")

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW5B", "3", "2", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "randArray.txt" file is generated
        file_path = "/autograder/source/randArray.txt"
        file_generated = os.path.isfile(file_path)

        # Standard unit test case with an associated error message
        if file_generated:
            print("PASSED!! Found output File 'randArray.txt'")
            self.assertTrue(True, msg="")
            os.remove(file_path)
        else:
            print("FAILED!! Could not Find output File 'randArray.txt'")
            self.assertTrue(False, msg="")

    # Associated point value within GradeScope
    @weight(0)
    def test05(self):
        # Title used by Gradescope 
        """HW5B - Testcase 1"""

        print(f"Running program\n\n$ ./HW5B 5 6 2\n")

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW5B", "5", "6", "2"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "randArray.txt" file is generated
        file_path = "/autograder/source/randArray.txt"
        file_generated = os.path.isfile(file_path)

        rand_out = subprocess.check_output(["head", "-n", "1", "/autograder/source/randArray.txt"]).decode('utf-8').strip()

        # Read the contents of randArray.txt and ref.csv
        if file_generated:
            rand_content = read_file_contents(file_path)

            print(f"Your Output: \n{rand_content}")

            # Standard unit test case with an associated error message
            if rand_out == "5 6":
                print("PASSED!!")
                self.assertTrue(True, msg="")
            else:
                print("FAILED!!")
                self.assertTrue(False, msg="")
        
            os.remove(file_path)

        else:
            # Print a message if randArray.txt is not generated
            print(f"\nFAILED!! Output file 'randArray.txt' could not be found.")
            self.assertTrue(False, msg="")
        
    # Associated point value within GradeScope
    @weight(0)
    def test06(self):
        # Title used by Gradescope 
        """HW5B - Testcase 2"""

        print(f"Running program\n\n$ ./HW5B 4 4 4\n")

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW5B", "4", "4", "4"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "randArray.txt" file is generated
        file_path = "/autograder/source/randArray.txt"
        file_generated = os.path.isfile(file_path)

        rand_out = subprocess.check_output(["head", "-n", "1", "/autograder/source/randArray.txt"]).decode('utf-8').strip()

        # Read the contents of randArray.txt and ref.csv
        if file_generated:
            rand_content = read_file_contents(file_path)

            print(f"Your Output: \n{rand_content}")

            # Standard unit test case with an associated error message
            if rand_out == "4 4":
                print("PASSED!!")
                self.assertTrue(True, msg="")
            else:
                print("FAILED!!")
                self.assertTrue(False, msg="")
        
            os.remove(file_path)

        else:
            # Print a message if randArray.txt is not generated
            print(f"\nFAILED!! Output file 'randArray.txt' could not be found.")
            self.assertTrue(False, msg="")
    
    # Associated point value within GradeScope
    @weight(0)
    def test07(self):
        # Title used by Gradescope 
        """HW5B - Testcase 3"""

        print(f"Running program\n\n$ ./HW5B 6 3 9\n")

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW5B", "6", "3", "9"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "randArray.txt" file is generated
        file_path = "/autograder/source/randArray.txt"
        file_generated = os.path.isfile(file_path)

        rand_out = subprocess.check_output(["head", "-n", "1", "/autograder/source/randArray.txt"]).decode('utf-8').strip()

        # Read the contents of randArray.txt and ref.csv
        if file_generated:
            rand_content = read_file_contents(file_path)

            print(f"Your Output:\n{rand_content}")

            # Standard unit test case with an associated error message
            if rand_out == "6 3":
                print("PASSED!!")
                self.assertTrue(True, msg="")
            else:
                print("FAILED!!")
                self.assertTrue(False, msg="")
        
            os.remove(file_path)

        else:
            # Print a message if randArray.txt is not generated
            print(f"\nFAILED!! Output file 'randArray.txt' could not be found.")
            self.assertTrue(False, msg="")

    # Associated point value within GradeScope
    @weight(2)
    def test08(self):
        # Title used by Gradescope 
        """HW5B - File I/O Formatting"""

        print(f"Running program\n\n$ ./HW5B 3 4 0\n")

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW5B", "3", "4", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "randArray.txt" file is generated
        file_path = "/autograder/source/randArray.txt"
        file_generated = os.path.isfile(file_path)

        # Read the contents of randArray.txt and ref.csv
        if file_generated:
            rand_content = read_file_contents(file_path)
            reference_content = read_file_contents("/autograder/source/reference/refRand.txt")

            # Compare the contents
            print(f"Expected Output:\n{reference_content}")
            print(f"Your Output: \n{rand_content}")

            # Standard unit test case with an associated error message
            if rand_content in reference_content:
                print("PASSED!! Contents of 'randArray.txt' are correct.")
                self.assertTrue(True, msg="")
            else:
                print("FAILED!! Contents of 'randArray.txt' are incorrect.")
                self.assertTrue(False, msg="")
        
            os.remove(file_path)

        else:
            # Print a message if randArray.txt is not generated
            print(f"\nFAILED!! Output file 'randArray.txt' could not be found.")
            self.assertTrue(False, msg="")

    # Associated point value within GradeScope
    @weight(0)
    def test09(self):
        #Title used by Gradescope 
        """HW5C - Compilation Test"""

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