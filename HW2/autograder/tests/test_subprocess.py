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

def extract_time_components(input_string):
    keyword = "The new time is: "
    index = input_string.find(keyword)

    if index != -1:
        time_part = input_string[index + len(keyword):]
        time_components = time_part.split()  # Split the time part into components

        if len(time_components) == 2:
            number, am_pm = time_components
            return number, am_pm
        else:
            return None, None  # Unexpected format
    else:
        return None, None  # Keyword not found in the input string

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
    @weight(1.0)
    def test09(self):
        #Title used by Gradescope 
        """HW2B - Backward Jump (Magnituide)"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        target = "9"

        # Example usage:
        time, meridian = extract_time_components(output)

        print(f"Started at 4 AM, moving Backwards in Time by 7 hrs\n\n### Expected ###\n{target} o'clock\n#### Found ####\n{time} o'clock")

        cat.kill()

        if target in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()

    # Associated point value within GradeScope
    @weight(1.5)
    def test10(self):
        #Title used by Gradescope 
        """HW2B - Backward Jump (Meridian)"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        target = "PM"

        # Example usage:
        time, meridian = extract_time_components(output)

        print(f"Started at 4 AM, moving Backwards in Time by 7 hrs\n\n### Expected ###\n{target}\n#### Found ####\n{meridian}")

        cat.kill()

        if target == meridian:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()

     # Associated point value within GradeScope
    @weight(1.0)
    def test11(self):
        #Title used by Gradescope 
        """HW2B - Backward Jump (Magnituide)"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        target = "9"

        # Example usage:
        time, meridian = extract_time_components(output)

        print(f"Started at 12 PM, moving Backwards in Time by 15 hrs\n\n### Expected ###\n{target} o'clock\n#### Found ####\n{time} o'clock")

        cat.kill()

        if target in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
    
    # Associated point value within GradeScope
    @weight(1.5)
    def test12(self):
        #Title used by Gradescope 
        """HW2B - Backward Jump (Meridian)"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        target = "PM"

        # Example usage:
        time, meridian = extract_time_components(output)

        print(f"Started at 12 PM, moving Backwards in Time by 15 hrs\n\n### Expected ###\n{target}\n#### Found ####\n{meridian}")

        cat.kill()

        if target == meridian:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()

    
    # Associated point value within GradeScope
    @weight(1.0)
    def test13(self):
        #Title used by Gradescope 
        """HW2B - Forward Jump (Magnitude)"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        target = "7"

        # Example usage:
        time, meridian = extract_time_components(output)

        print(f"Started at 7 AM, moving Forwards in Time by 240 hrs\n\n### Expected ###\n{target} o'clock\n#### Found ####\n{time} o'clock")

        cat.kill()

        if target in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
    
    # Associated point value within GradeScope
    @weight(1.5)
    def test14(self):
        #Title used by Gradescope 
        """HW2B - Forward Jump (Meridian)"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        target = "AM"

        # Example usage:
        time, meridian = extract_time_components(output)

        print(f"Started at 7 AM, moving Forwards in Time by 240 hrs\n\n### Expected ###\n{target}\n#### Found ####\n{meridian}")

        cat.kill()

        if target == meridian:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
    
    # Associated point value within GradeScope
    @weight(1.0)
    def test15(self):
        #Title used by Gradescope 
        """HW2B - Forward Jump (Magnitude)"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        target = "7"

        # Example usage:
        time, meridian = extract_time_components(output)

        print(f"Started at 1 PM, moving Forwards in Time by 6 hrs\n\n### Expected ###\n{target} o'clock\n#### Found ####\n{time} o'clock")

        cat.kill()

        if target in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
    
    # Associated point value within GradeScope
    @weight(1.5)
    def test16(self):
        #Title used by Gradescope 
        """HW2B - Forward Jump (Meridian)"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        target = "PM"

        # Example usage:
        time, meridian = extract_time_components(output)

        print(f"Started at 1 PM, moving Forwards in Time by 6 hrs\n\n### Expected ###\n{target}\n#### Found ####\n{meridian}")

        cat.kill()

        if target == meridian:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()

    # Associated point value within GradeScope
    @weight(0)
    def test17(self):
        #Title used by Gradescope 
        """HW2B - I/O Formatting"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB5.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2B"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB5.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        ref.kill()

        print(f"Started at 2 PM, moving Forwards/Backwards in Time by 0 hrs\n")


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
    def test18(self):
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
    
    # Associated point value within GradeScope
    @weight(1)
    def test19(self):
        #Title used by Gradescope 
        """HW2C - Invalid Input"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inC4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2C"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "1", "/autograder/source/reference/refC4.txt"]).decode('utf-8').strip()

        cat.kill()

        print(f"Input Sequence: -4, -1\n")

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
    def test20(self):
        #Title used by Gradescope 
        """HW2C - Exit"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inC3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2C"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!! Program did not exit."

        ref = subprocess.Popen(["cat", "/autograder/source/reference/refC3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        ref.kill()
        
        print(f"Input: -1\n")

        result = compare_strings(output, reference)
        print(result)

        target = "OK, Goodbye."

        # Standard unit test case with an associated error message
        if target.lower() in output.lower():
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

        cat.terminate()
        ref.terminate()

    # Associated point value within GradeScope
    @weight(0)
    def test21(self):
        #Title used by Gradescope 
        """HW2C - Testcase - 1"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inC1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2C"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!!"

        print(f"Input Sequence = 4, 3, 2, 1, 0, -1\n\nYour Output\n\n{output}")

        # Standard unit test case with an associated error message
        if output.lower().endswith("ok, goodbye."):
            print("\nProgram Exit Succesfully!!")
            self.assertTrue(True, msg="")
        else:
            print("\nProgram did not Exit Successfully!!")
            self.assertTrue(False, msg="")

        cat.terminate()
    
    # Associated point value within GradeScope
    @weight(0)
    def test22(self):
        #Title used by Gradescope 
        """HW2C - Testcase - 2"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inC2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2C"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!!"

        print(f"Input Sequence = 4, 4, 4, 4, -1\n\nYour Output\n\n{output}")

        # Standard unit test case with an associated error message
        if output.lower().endswith("ok, goodbye."):
            print("\nProgram Exit Succesfully!!")
            self.assertTrue(True, msg="")
        else:
            print("\nProgram did not Exit Successfully!!")
            self.assertTrue(False, msg="")

        cat.terminate()
    
    # Associated point value within GradeScope
    @weight(0)
    def test23(self):
        #Title used by Gradescope 
        """HW2C - Testcase - 3"""

        # Create a subprocess to run the students code and with our test file
        cat = subprocess.Popen(["cat", "/autograder/source/input/inC5.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Use subprocess.run to execute the command with a timeout
        try:
            test = subprocess.run(["./HW2C"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            cat.kill()
            output = "Timeout expired!!"

        print(f"Input Sequence = 1, 2, 3, 4, 5, -1\n\nYour Output\n\n{output}")

        # Standard unit test case with an associated error message
        if output.lower().endswith("ok, goodbye."):
            print("\nProgram Exit Succesfully!!")
            self.assertTrue(True, msg="")
        else:
            print("\nProgram did not Exit Successfully!!")
            self.assertTrue(False, msg="")

        cat.terminate()