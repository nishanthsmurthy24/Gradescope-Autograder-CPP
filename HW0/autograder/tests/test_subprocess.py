import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
from difflib import Differ

def compare_strings(string1, string2):
    differ = Differ()
    diff = list(differ.compare(string1.splitlines(), string2.splitlines()))
    return '\n'.join(diff)

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    # Associated point value within GradeScope
    @weight(5)
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
        else:
            print("COMPILATION SUCCESSFUL!!")
        
        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test01(self):
        #Title used by Gradescope 
        """Testcase - 1"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "in1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW0"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        ref = subprocess.Popen(["cat", "reference1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        test.kill()
        cat.kill()
        ref.kill()

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")

        test.terminate()
        cat.terminate()
        ref.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test02(self):
        #Title used by Gradescope 
        """Testcase - 2"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "in2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW0"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        ref = subprocess.Popen(["cat", "reference2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        test.kill()
        cat.kill()
        ref.kill()

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")

        test.terminate()
        cat.terminate()
        ref.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test03(self):
        #Title used by Gradescope 
        """Testcase - 3"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "in3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW0"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        ref = subprocess.Popen(["cat", "reference3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        test.kill()
        cat.kill()
        ref.kill()

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")

        test.terminate()
        cat.terminate()
        ref.terminate()
        

    # Associated point value within GradeScope
    @weight(1)
    def test04(self):
        #Title used by Gradescope 
        """Testcase - 4"""

        # Create a subprocess to run the students code and with our test file 
        cat = subprocess.Popen(["cat", "in4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["./HW0"], stdin= cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        ref = subprocess.Popen(["cat", "reference4.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        test.kill()
        cat.kill()
        ref.kill()

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")

        test.terminate()
        cat.terminate()
        ref.terminate()