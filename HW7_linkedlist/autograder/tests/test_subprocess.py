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
    @weight(0)
    def test00(self):
        #Title used by Gradescope 
        """Compilation Test"""

        # Create a subprocess to run the students make file to ensure it compiles 
        test = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stderr.read().strip().decode('utf-8')
        test.kill()

        # Standard unit test case with an associated error message 
        self.assertTrue( output == "", msg=output)
        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test01(self):
        #Title used by Gradescope 
        """Testcase - 1 (Short CSV - Zipcode)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4-short.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "98072" in output:
            print("PASSED!!\nZipcode: 98072 Found!!")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\nZipcode: 98072 not Found!!")
            self.assertTrue(False, msg="")

        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test02(self):
        #Title used by Gradescope 
        """Testcase - 2 (Short CSV - Average Price)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4-short.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "556000" in output:
            print("PASSED!!\n***Expected***\n98126:average price=556000\n\n****Found****\n98126:average price=556000")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\n***Expexted***\n98126:average price=556000")
            self.assertTrue(False, msg="")

        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test03(self):
        #Title used by Gradescope 
        """Testcase - 3 (Long CSV - Zipcode)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "98168" in output:
            print("PASSED!!\nZipcode: 98168 Found!!")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\nZipcode: 98168 not Found!!")
            self.assertTrue(False, msg="")
        
        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test04(self):
        #Title used by Gradescope 
        """Testcase - 4 (Long CSV - Zipcode)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "98023" in output:
            print("PASSED!!\nZipcode: 98023 Found!!")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\nZipcode: 98023 not Found!!")
            self.assertTrue(False, msg="")

        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test05(self):
        #Title used by Gradescope 
        """Testcase - 5 (Long CSV - Zipcode)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "98059" in output:
            print("PASSED!!\nZipcode: 98059 Found!!")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\nZipcode: 98059 not Found!!")
            self.assertTrue(False, msg="")
        
        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test06(self):
        #Title used by Gradescope 
        """Testcase - 6 (Long CSV - Zipcode)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "98031" in output:
            print("PASSED!!\nZipcode: 98031 Found!!")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\nZipcode: 98031 not Found!!")
            self.assertTrue(False, msg="")

        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test07(self):
        #Title used by Gradescope 
        """Testcase - 7 (Long CSV - Average Price)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "296472" in output:
            print("PASSED!!\n***Expected***\n98003:average price=296472\n\n****Found****\n98003:average price=296472")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\n***Expected***\n98003:average price=296472")
            self.assertTrue(False, msg="")

        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test08(self):
        #Title used by Gradescope 
        """Testcase - 8 (Long CSV - Average Price)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "244430" in output:
            print("PASSED!!\n***Expected***\n98168:average price=244430\n\n****Found****\n98168:average price=244430")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\n***Expected***\n98168:average price=244430")
            self.assertTrue(False, msg="")

        test.terminate()
    
    # Associated point value within GradeScope
    @weight(1)
    def test09(self):
        #Title used by Gradescope 
        """Testcase - 9 (Long CSV - Average Price)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "294164" in output:
            print("PASSED!!\n***Expected***\n98030:average price=294164\n\n****Found****\n98030:average price=294164")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\n***Expected***\n98030:average price=294164")
            self.assertTrue(False, msg="")

        test.terminate()

    # Associated point value within GradeScope
    @weight(1)
    def test10(self):
        #Title used by Gradescope 
        """Testcase - 10 (Long CSV - Average Price)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        test.kill()

        # Standard unit test case with an associated error message
        if "427729" in output:
            print("PASSED!!\n***Expected***\n98118:average price=427729\n\n****Found****\n98118:average price=427729")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!!\n***Expected***\n98118:average price=427729")
            self.assertTrue(False, msg="")

        test.terminate()

    # Associated point value within GradeScope
    @weight(0)
    def test11(self):
        #Title used by Gradescope 
        """Testcase - 11 (Short CSV - I/O Formatting)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4-short.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        ref = subprocess.Popen(["cat", "reference1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        test.kill()
        ref.kill()

        result = compare_strings(output, reference)
        print(result)

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")

        test.terminate()
        ref.terminate()
    
    # Associated point value within GradeScope
    @weight(0)
    def test12(self):
        #Title used by Gradescope 
        """Testcase - 12 (Long CSV - I/O Formatting)"""

        # Create a subprocess to run the students code and with our test file 
        test = subprocess.Popen(["./HW7", "house-info-v4.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            output, _ = test.communicate(timeout=10)
            output = output.strip().decode('utf-8')
        except subprocess.TimeoutExpired:
            test.kill()
            output = "Timeout expired!!"

        ref = subprocess.Popen(["cat", "reference2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        reference = ref.stdout.read().strip().decode('utf-8')

        test.kill()
        ref.kill()

        result = compare_strings(output, reference)
        print(result)

        # print(f"***Expected***\n{reference}\n\n****Found****\n{output}")

        # Standard unit test case with an associated error message
        if(self.assertTrue(output == reference, msg="")):
            print("\nFAILED!!")
        else:
            print("\nPASSED!!")

        test.terminate()
        ref.terminate()

    # # Associated point value within GradeScope
    # @weight(0)
    # def test9(self):
    #     #Title used by Gradescope 
    #     """Valgrind - Memory Leak Test"""

    #     # Create a subprocess to run the students code and with our test file 
    #     test = subprocess.Popen(["valgrind", "--tool=memcheck", "--leak-check=full", "./HW7", "house-info-v4-short.csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     try:
    #         output, _ = test.communicate(timeout=10)
    #         output = output.strip().decode('utf-8')
    #     except subprocess.TimeoutExpired:
    #         test.kill()
    #         output = "Timeout expired!!"

    #     # Standard unit test case with an associated error message
    #     if(self.assertTrue("All heap blocks were freed" in output, msg="")):
    #         print("FAILED!!")
    #     else:
    #         print("PASSED!!")

    #     print(output)

    #     test.kill()

    #     # Standard unit test case with an associated error message

    #     test.terminate()