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
        """Compilation Test"""

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["make", "midterm"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
    @weight(5)
    def test01(self):
        # Title used by Gradescope 
        """Output File - 'power12.txt' """

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/in1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./midterm_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "power12.txt" file is generated
        file_path = "/autograder/source/power12.txt"
        file_generated = os.path.isfile(file_path)

        # Standard unit test case with an associated error message
        if file_generated:
            print("PASSED!! Found output File 'power12.txt'")
            os.remove(file_path)
            self.assertTrue(True, msg="")
        else:
            print("FAILED!! Could not Find output File 'power12.txt'")
            self.assertTrue(False, msg="")
    
    # Associated point value within GradeScope
    @weight(0)
    def test02(self):
        # Title used by Gradescope 
        """Testcase 1 - Contents of 'power12.txt' """

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/in1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./midterm_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "power12.txt" file is generated
        file_path = "/autograder/source/power12.txt"
        file_generated = os.path.isfile(file_path)

        # Read the contents of power12.txt and ref.txt
        if file_generated:
            file_content = read_file_contents(file_path)
            reference_content = read_file_contents("/autograder/source/reference/ref1.txt")

            # Compare the contents
            result = compare_strings(file_content, reference_content, 3)
            print(result)

            # Standard unit test case with an associated error message
            if file_content == reference_content:
                print("\nPASSED!! Contents of 'power12.txt' are correct.")
                os.remove(file_path)
                self.assertTrue(True, msg="")
            else:
                print("\nFAILED!! Contents of 'power12.txt' are incorrect.")
                self.assertTrue(False, msg="")
        else:
            # Print a message if power12.txt is not generated
            print(f"\nFAILED!! Ouput file 'power12.txt' could not be found.")
            self.assertTrue(False, msg="")
    
    # Associated point value within GradeScope
    @weight(0)
    def test03(self):
        # Title used by Gradescope 
        """Testcase 1 - Output' """

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/in1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./midterm_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        file_path = "/autograder/source/power12.txt"

        # Read the contents of power12.txt and ref.txt
        reference_out = read_file_contents("/autograder/source/reference/out1.txt")

        # Compare the contents
        result = compare_strings(output, reference_out, 6)
        print(result)

        # Standard unit test case with an associated error message
        if output in reference_out:
            print("\nPASSED!! cout statements are correct.")
            os.remove(file_path)
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!! cout statements are incorrect.")
            self.assertTrue(False, msg="")

    # Associated point value within GradeScope
    @weight(0)
    def test04(self):
        # Title used by Gradescope 
        """Testcase 2 - Contents of 'power12.txt' """

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/in2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./midterm_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "power12.txt" file is generated
        file_path = "/autograder/source/power12.txt"
        file_generated = os.path.isfile(file_path)

        # Read the contents of power12.txt and ref.txt
        if file_generated:
            file_content = read_file_contents(file_path)
            reference_content = read_file_contents("/autograder/source/reference/ref2.txt")

            # Compare the contents
            result = compare_strings(file_content, reference_content, 5)
            print(result)

            # Standard unit test case with an associated error message
            if file_content == reference_content:
                print("\nPASSED!! Contents of 'power12.txt' are correct.")
                os.remove(file_path)
                self.assertTrue(True, msg="")
            else:
                print("\nFAILED!! Contents of 'power12.txt' are incorrect.")
                self.assertTrue(False, msg="")
        else:
            # Print a message if power12.txt is not generated
            print(f"\nFAILED!! Ouput file 'power12.txt' could not be found.")
            self.assertTrue(False, msg="")

    # Associated point value within GradeScope
    @weight(0)
    def test05(self):
        # Title used by Gradescope 
        """Testcase 2 - Output' """

        try:
            # Run the program and capture the output
            cat = subprocess.Popen(["cat", "/autograder/source/input/in2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./midterm_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        file_path = "/autograder/source/power12.txt"

        # Read the contents of power12.txt and ref.txt
        reference_out = read_file_contents("/autograder/source/reference/out2.txt")

        # Compare the contents
        result = compare_strings(output, reference_out, 8)
        print(result)

        # Standard unit test case with an associated error message
        if output in reference_out:
            print("\nPASSED!! cout statements are correct.")
            os.remove(file_path)
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!! cout statements are incorrect.")
            self.assertTrue(False, msg="")

    
    # Associated point value within GradeScope
    @weight(0)
    def test06(self):
        #Title used by Gradescope 
        """Terminal Output (I/O Formatting)"""

        try:
            cat = subprocess.Popen(["cat", "/autograder/source/input/in3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./midterm_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "1", "/autograder/source/reference/out3.txt"]).decode('utf-8').strip()

        result = compare_strings(output, reference, 1)
        print(result)

        # Standard unit test case with an associated error message
        if reference == output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")
        
        file_path = "/autograder/source/power12.txt"
        os.remove(file_path)