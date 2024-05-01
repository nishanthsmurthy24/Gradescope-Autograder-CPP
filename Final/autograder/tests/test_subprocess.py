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
        test = subprocess.Popen(["make", "final"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
        """Basic Testcase"""

        try:
            cat = subprocess.Popen(["cat", "/autograder/source/input/in1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./final_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        print(f"<Number of Cars>\n\n<Model>\n<Tank Capacity> <MPG>\n<Refuel Quantity>\n<Miles to Drive>\n")

        print(f"2\n\nSuburban\n44.0 12.0\n22\n24\n\nPrius\n10.0 50.0\n10\n200\n")

        reference = subprocess.check_output(["head", "-n", "2", "/autograder/source/reference/ref1.txt"]).decode('utf-8').strip()

        cat.kill()

        result = compare_strings(output, reference, 2)
        print(result)

        # Standard unit test case with an associated error message
        if reference == output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()

    # Associated point value within GradeScope
    @weight(0)
    def test02(self):
        #Title used by Gradescope 
        """Default Testcase"""

        try:
            cat = subprocess.Popen(["cat", "/autograder/source/input/in2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./final_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        print(f"<Number of Cars>\n\n<Make> <Model>\n<Tank Capacity> <MPG>\n<Refuel Quantity>\n<Miles to Drive>\n")
    
        print(f"2\n\nChevy Suburban\n44.0 12.0\n22\n24\n\nToyota Prius\n10.0 50.0\n10\n200\n")


        reference = subprocess.check_output(["head", "-n", "2", "/autograder/source/reference/ref2.txt"]).decode('utf-8').strip()

        cat.kill()

        result = compare_strings(output, reference, 2)
        print(result)

        # Standard unit test case with an associated error message
        if reference == output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()

    # Associated point value within GradeScope
    @weight(0)
    def test03(self):
        #Title used by Gradescope 
        """Testcase - 1"""

        try:
            cat = subprocess.Popen(["cat", "/autograder/source/input/in3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./final_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."
        
        print(f"<Number of Cars>\n\n<Make> <Model>\n<Tank Capacity> <MPG>\n<Refuel Quantity>\n<Miles to Drive>\n")

        print(f"5\n\nChevy Camaro\n40.0 18.5\n2.5\n100\n\nToyota Corolla\n20.0 28.9\n10\n200\n\nDodge Charger\n20.0 23.5\n5\n10.5\n\nPorsche 911\n16.9 18\n5\n89.5\n\nAudi A6\n30.0 20.8\n32.0\n189.5\n")

        reference = subprocess.check_output(["head", "-n", "5", "/autograder/source/reference/ref3.txt"]).decode('utf-8').strip()

        cat.kill()

        result = compare_strings(output, reference, 5)
        print(result)

        # Standard unit test case with an associated error message
        if reference == output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()

    # Associated point value within GradeScope
    @weight(0)
    def test04(self):
        #Title used by Gradescope 
        """Testcase - 2"""

        try:
            cat = subprocess.Popen(["cat", "/autograder/source/input/in4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            test = subprocess.run(["./final_exe"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        print(f"<Number of Cars>\n\n<Make> <Model>\n<Tank Capacity> <MPG>\n<Refuel Quantity>\n<Miles to Drive>\n")

        print(f"0\n")


        reference = subprocess.check_output(["head", "-n", "1", "/autograder/source/reference/ref4.txt"]).decode('utf-8').strip()

        cat.kill()

        result = compare_strings(output, reference, 1)
        print(result)

        # Standard unit test case with an associated error message
        if reference == output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()
    