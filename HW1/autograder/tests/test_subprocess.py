import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
from difflib import Differ
import re

def find_float(input_string, target_string):
    pattern = re.compile(f'{target_string}\s*([-+]?\d*\.\d+|\d+)')

    match = pattern.search(input_string)

    if match:
        float_value = float(match.group(1))
        return float_value
    else:
        print("Floating-point value not found.")

def compare_strings(string1, string2):
    differ = Differ()
    diff = list(differ.compare(string1.splitlines(), string2.splitlines()))
    return '\n'.join(diff)

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    # Associated point value within GradeScope
    @weight(0)
    def test00(self):
        #Title used by Gradescope 
        """HW1A - Compilation Test"""

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
    @weight(0.5)
    def test01(self):
        #Title used by Gradescope 
        """HW1A - Testcase 1 - Tank Volume"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1A"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        cat.kill()
        test.kill()

        target = "523.60"

        found = find_float(output, "Volume of the entire tank: ")
        print(f"Radius of the Sphere: 5\nHeight of the fluid: 4\n\n### Expected ###\nVolume of the entire tank: {target}\n#### Found ####\nVolume of the entire tank: {found}")

        # Standard unit test case with an associated error message
        if target in output:
            self.assertTrue(True, msg="")
        elif "523.59" in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
        test.terminate()

    # Associated point value within GradeScope
    @weight(0.5)
    def test02(self):
        #Title used by Gradescope 
        """HW1A - Testcase 1 - Tank Surface Area"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1A"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        cat.kill()
        test.kill()

        target = "314.16"

        found = find_float(output, "Surface area of the entire tank: ")
        print(f"### Expected ###\nSurface area of the entire tank: {target}\n#### Found ####\nSurface area of the entire tank: {found}")

        # Standard unit test case with an associated error message
        if target in output:
            self.assertTrue(True, msg="")
        elif "314.15" in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(0.5)
    def test03(self):
        #Title used by Gradescope 
        """HW1A - Testcase 1 - Volume Fluid"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1A"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        cat.kill()
        test.kill()

        target = "184.31"

        found = find_float(output, "Volume of the fluid: ")
        print(f"### Expected ###\nVolume of the fluid: {target}\n#### Found ####\nVolume of the fluid: {found}")
        
        # Standard unit test case with an associated error message
        if target in output:
            self.assertTrue(True, msg="")
        elif "184.30" in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
        test.terminate()

    # Associated point value within GradeScope
    @weight(0.5)
    def test04(self):
        #Title used by Gradescope 
        """HW1A - Testcase 1 - Surface Area Fluid"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1A"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        cat.kill()
        test.kill()

        target = "125.66"

        found = find_float(output, "Surface area covered by the fluid: ")
        print(f"### Expected ###\nSurface area covered by the fluid: {target}\n#### Found ####\nSurface area covered by the fluid: {found}")

        # Standard unit test case with an associated error message
        if target in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
        test.terminate()
    

    # Associated point value within GradeScope
    @weight(0.5)
    def test05(self):
        #Title used by Gradescope 
        """HW1A - Testcase 2 - Tank Volume"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1A"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        cat.kill()
        test.kill()

        target = "12770.05"

        found = find_float(output, "Volume of the entire tank: ")
        print(f"Radius of the Sphere: 14.5\nHeight of the fluid: 6.25\n\n### Expected ###\nVolume of the entire tank: {target}\n#### Found ####\nVolume of the entire tank: {found}")

        # Standard unit test case with an associated error message
        if target in output:
            self.assertTrue(True, msg="")
        elif "12770.04" in output:
            self.assertTrue(True, msg="")            
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
        test.terminate()

    # Associated point value within GradeScope
    @weight(0.5)
    def test06(self):
        #Title used by Gradescope 
        """HW1A - Testcase 2 - Tank Surface Area"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1A"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        cat.kill()
        test.kill()

        target = "2642.08"

        found = find_float(output, "Surface area of the entire tank: ")
        print(f"### Expected ###\nSurface area of the entire tank: {target}\n#### Found ####\nSurface area of the entire tank: {found}")

        # Standard unit test case with an associated error message
        if target in output:
            self.assertTrue(True, msg="")
        elif "2642.07" in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
        test.terminate()
    

    # Associated point value within GradeScope
    @weight(0.5)
    def test07(self):
        #Title used by Gradescope 
        """HW1A - Testcase 2 - Volume Fluid"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1A"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        cat.kill()
        test.kill()

        target = "1523.75"

        found = find_float(output, "Volume of the fluid: ")
        print(f"### Expected ###\nVolume of the fluid: {target}\n#### Found ####\nVolume of the fluid: {found}")
        
        # Standard unit test case with an associated error message
        if target in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(0.5)
    def test08(self):
        #Title used by Gradescope 
        """HW1A - Testcase 2 - Surface Area Fluid"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1A"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        cat.kill()
        test.kill()

        target = "569.41"

        found = find_float(output, "Surface area covered by the fluid: ")
        print(f"### Expected ###\nSurface area covered by the fluid: {target}\n#### Found ####\nSurface area covered by the fluid: {found}")

        # Standard unit test case with an associated error message
        if target in output:
            self.assertTrue(True, msg="")
        else:
            self.assertTrue(False, msg="")

        cat.terminate()
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(0)
    def test09(self):
        #Title used by Gradescope 
        """HW1A - I/O Formatting"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inA1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1A"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"
        
        ref = subprocess.Popen(["cat", "/autograder/source/reference/refA1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        test.kill()
        ref.kill()

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")

        cat.terminate()
        test.terminate()
        ref.terminate()
    
    # Associated point value within GradeScope
    @weight(0)
    def test10(self):
        #Title used by Gradescope 
        """HW1B - Compilation Test"""

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
    def test11(self):
        #Title used by Gradescope 
        """HW1B - Float to Integer"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1B"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"
    
        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        test.kill()
        ref.kill()

        print(f"Input: f\nR = 0.4, G = 0, B = 1\n\n")

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")
        
        cat.terminate()
        test.terminate()
        ref.terminate()
    
    # Associated point value within GradeScope
    @weight(1)
    def test12(self):
        #Title used by Gradescope 
        """HW1B - Float to Integer"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1B"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"
    
        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        test.kill()
        ref.kill()

        print(f"Input: f\nR = 0.27, G = 0.87, B = 32\n\n")

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")
        
        cat.terminate()
        test.terminate()
        ref.terminate()
    
    # Associated point value within GradeScope
    @weight(1)
    def test13(self):
        #Title used by Gradescope 
        """HW1B - Integer to Float"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1B"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"
    
        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        test.kill()
        ref.kill()

        print(f"Input: i\nR = 255, G = 0, B = 255\n\n")

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")
        
        cat.terminate()
        test.terminate()
        ref.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test14(self):
        #Title used by Gradescope 
        """HW1B - Integer to Float"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB5.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1B"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"
    
        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB5.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        test.kill()
        ref.kill()

        print(f"Input: i\nR = 40, G = 254, B = 98\n\n")

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")
        
        cat.terminate()
        test.terminate()
        ref.terminate()

    # Associated point value within GradeScope
    @weight(0.5)
    def test15(self):
        #Title used by Gradescope 
        """HW1B - Invalid Option"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1B"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"
    
        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        test.kill()
        ref.kill()

        print(f"Input: j\n\n")

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")
        
        cat.terminate()
        test.terminate()
        ref.terminate()

    # Associated point value within GradeScope
    @weight(0.5)
    def test16(self):
        #Title used by Gradescope 
        """HW1B - Invalid Option"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "/autograder/source/input/inB6.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW1B"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"
    
        ref = subprocess.Popen(["cat", "/autograder/source/reference/refB6.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        cat.kill()
        test.kill()
        ref.kill()

        print(f"Input: 6\n\n")

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")
        
        cat.terminate()
        test.terminate()
        ref.terminate()   