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
        """HW4A - Compilation Test"""

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
            print(f"\nInput File - grades.txt\n")
            print(f"Kelden Amadiro 57\nDaneel Olivaw 89.0\nElijah Baley 84\nGiskard Reventlov 88.8\nAlfred Lanning 68")
            print(f"Susan Calvin 94\nHan Fastolfe 92\nGregory Powell 73\nMike Donovan 67\nLaurance Robertson 76")
            print(f"Hari Seldon 98\nDors Venabili 82\nEto Demerzel 89.0\nRaych Seldon 78\nSalvor Hardin 86\nYugo Amaryl 96")
            print(f"Ebling Mis 87\nJohn Watson 43\nSherlock Holmes 92\nViolet Crawley 83\nGreg Lestrade 74\nMissus Hudson 85")
            print(f"Jim Moriarty 99.99999999999\nMolly Hooper 65\nIrene Adler 91\nMycroft Holmes 82\nTom Branson 83\nJohn Bates 89\nMister Carson 79")
        
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(1)
    def test01(self):
        # Title used by Gradescope 
        """HW4A - Output File - 'statistics.csv' """

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW4A"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "statistics.csv" file is generated
        file_path = "/autograder/source/statistics.csv"
        file_generated = os.path.isfile(file_path)

        # Standard unit test case with an associated error message
        if file_generated:
            print("PASSED!! Found output File 'statistics.csv'")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!! Could not Find output File 'statistics.csv'")
            self.assertTrue(False, msg="")
    
    # Associated point value within GradeScope
    @weight(6)
    def test02(self):
        # Title used by Gradescope 
        """HW4A - Contents of 'statistics.csv' """

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW4A"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "statistics.csv" file is generated
        file_path = "/autograder/source/statistics.csv"
        file_generated = os.path.isfile(file_path)

        # Read the contents of statistics.csv and ref.csv
        if file_generated:
            statistics_content = read_file_contents(file_path)
            reference_content = read_file_contents("/autograder/source/reference/refStats.csv")

            # Compare the contents
            result = compare_strings(statistics_content, reference_content, 6)
            print(result)

            # Standard unit test case with an associated error message
            if statistics_content in reference_content:
                print("\nPASSED!! Contents of 'statistics.csv' are correct.")
                self.assertTrue(True, msg="")
            else:
                print("\nFAILED!! Contents of 'statistics.csv' are incorrect.")
                self.assertTrue(False, msg="")
        else:
            # Print a message if statistics.csv is not generated
            print(f"\nFAILED!! Statistics file 'statistics.csv' could not be found.")
            self.assertTrue(False, msg="")
        
    # Associated point value within GradeScope
    @weight(2)
    def test03(self):
        #Title used by Gradescope 
        """HW4A - Terminal Output (I/O Formatting)"""

        try:
            test = subprocess.run(["./HW4A"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "5", "/autograder/source/reference/refA.txt"]).decode('utf-8').strip()

        result = compare_strings(output, reference, 5)
        print(result)

        # Standard unit test case with an associated error message
        if reference == output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

    # Associated point value within GradeScope
    @weight(0)
    def test05(self):
        #Title used by Gradescope 
        """HW4B - Compilation Test"""

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
            # Check if "statistics.csv" file is generated
            file_path = "/autograder/source/statistics.csv"
            with open(file_path, 'w') as file:
                file.write("Grade,NumStudents\nA,6\nB,9\nC,4\nD,2\nF,1")
            print(f"\nInput File - statistics.csv\n")
            print(f"Grade,NumStudents\nA,6\nB,9\nC,4\nD,2\nF,1")

        test.terminate()
    
    # Associated point value within GradeScope
    @weight(1)
    def test06(self):
        # Title used by Gradescope 
        """HW4B - Output File - 'histogram.txt' """

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW4B"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "histogram.txt" file is generated
        file_path = "/autograder/source/histogram.txt"
        file_generated = os.path.isfile(file_path)

        # Standard unit test case with an associated error message
        if file_generated:
            print("PASSED!! Found output File 'histogram.txt'")
            self.assertTrue(True, msg="")
        else:
            print("FAILED!! Could not Find output File 'histogram.txt'")
            self.assertTrue(False, msg="")
    
    # Associated point value within GradeScope
    @weight(0)
    def test07(self):
        # Title used by Gradescope 
        """HW4B - Contents of 'histogram.txt' """

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW4B"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "histogram.txt" file is generated
        file_path = "/autograder/source/histogram.txt"
        file_generated = os.path.isfile(file_path)

        # Read the contents of histogram.txt and ref.txt
        if file_generated:
            statistics_content = read_file_contents(file_path)
            reference_content = read_file_contents("/autograder/source/reference/refHisto.txt")

            # Compare the contents
            # result = compare_strings(statistics_content, reference_content, 6)
            print(f"Expected Output:\n\n{reference_content}")
            print(f"\nYour Output:\n\n{statistics_content}")

            self.assertTrue(True, msg="")
            
        else:
            # Print a message if statistics.csv is not generated
            print(f"\nFAILED!! Statistics file 'histogram.txt' could not be found.")
            self.assertTrue(False, msg="")

    # Associated point value within GradeScope
    @weight(0)
    def test08(self):
        #Title used by Gradescope 
        """HW4C - Compilation Test"""

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
            print(f"\nInput File - input_files/blahblah.txt\n")
            print("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut aliquam ac metus eget maximus. Suspendisse eget tincidunt ligula. Fusce aliquet leo nec bibendum tempor.") 
            print("Cras elit dolor, aliquet non lacus a, vestibulum eleifend urna. Integer ultrices ex ac vulputate tristique. Vestibulum felis libero, lacinia at purus ut, convallis eleifend mi.")
            print("Vestibulum in euismod orci, a euismod augue. Integer quam velit, lobortis sit amet malesuada sit amet, dignissim eget odio. Proin eu eros eget magna eleifend pellentesque ac nec tortor.")
            print("Nunc mattis turpis et leo cursus, sit amet dictum nisl pellentesque. Cras ultricies leo tellus, a volutpat ipsum maximus at. Pellentesque aliquet, lorem eu gravida tincidunt,")
            print("magna tortor laoreet est, at aliquam magna nisl in nisl. Praesent eget pretium dolor. Aliquam euismod, enim nec cursus maximus, nunc massa molestie ipsum, sed posuere dolor leo ut neque.")
            print("Vestibulum id tortor nec justo venenatis tristique id et est. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eget mollis augue.")
            print("Nunc sem arcu, feugiat id porttitor sed, fermentum ac nunc. Vivamus lacinia ante vitae lacus commodo gravida. Praesent eget eros quis felis efficitur faucibus a ut nulla. Sed non accumsan ipsum.")
            print("Praesent condimentum dolor rhoncus massa hendrerit vulputate. Nunc euismod congue quam. In nisl erat, vulputate ac metus hendrerit, congue varius metus. Sed leo felis, eleifend eget pulvinar eget,")
            print("ultrices malesuada lorem. Ut massa leo, ullamcorper quis velit vel, vestibulum blandit tortor. Sed consequat semper pulvinar. In massa enim, suscipit eu vestibulum quis, feugiat id ante.")
            print("Pellentesque nec dictum nisi, ut pretium quam. Aenean ut vestibulum mi, nec dapibus metus. Quisque rhoncus ex nulla, vel bibendum turpis tristique vitae. Vestibulum vel dolor libero.")
            print("Etiam mauris sem, dignissim a libero in, ultricies sagittis ex. Vestibulum quis est mi. Sed at augue at lacus tristique rutrum. Aenean eu magna vitae orci rhoncus tincidunt eget sit amet massa.")
            print("Donec eleifend lobortis turpis commodo sodales. Vestibulum sed tellus vel justo cursus ultricies sed at arcu. Curabitur iaculis id nisl eget mollis. Donec et sem at metus commodo molestie.")
            print("Morbi sed congue odio. Fusce tempus sem a nulla congue, non vestibulum mi ornare. Proin eu purus vitae velit laoreet lacinia non quis metus. Cras at nisl non risus varius bibendum nec eget nulla.")
            print("Morbi congue ac nulla eu viverra. Sed placerat faucibus mauris a ultricies. Sed pretium lorem at ex dapibus, eget lacinia nisl pretium. Integer sodales vehicula arcu sit amet interdum.")
            print("Cras accumsan in magna at commodo. Suspendisse pretium velit vitae pellentesque posuere. Aliquam erat volutpat. Sed elementum urna eget justo faucibus, vel egestas magna hendrerit.")
            print("Nullam volutpat tristique erat, ac aliquam nunc gravida vitae. Nunc ut libero gravida, rhoncus sapien ornare, molestie massa. Proin id dignissim nulla. Suspendisse euismod posuere lacus convallis suscipit.")
            print("Sed dapibus elit arcu, sit amet posuere ex tincidunt nec. Nunc vel purus massa. Nullam scelerisque quam sed lacus finibus cursus. Ut tincidunt turpis eleifend finibus lobortis. Mauris aliquet finibus bibendum.")
        
        os.mkdir("/autograder/source/output_files")
        
        test.terminate()

    # Associated point value within GradeScope
    @weight(2)
    def test09(self):
        # Title used by Gradescope 
        """HW4C - Output File - 'election_results.txt' """

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW4C"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "election_results.txt" file is generated
        file_path = "/autograder/source/output_files/election_results.txt"
        file_generated = os.path.isfile(file_path)

        missed_file_path = "/autograder/source/election_results.txt"
        file_generated_wrong_path = os.path.isfile(missed_file_path)

        # Standard unit test case with an associated error message
        if file_generated:
            print("PASSED!! Found output File 'output_files/election_results.txt'")
            self.assertTrue(True, msg="")
        elif missed_file_path:
            print("FAILED!! Found output File 'election_results.txt' in the root directory. It needs to be in 'output_files' directory.")
            self.assertTrue(False, msg="")
        else:
            print("FAILED!! Could not Find output File 'election_results.txt'")
            self.assertTrue(False, msg="")
    
    # Associated point value within GradeScope
    @weight(5)
    def test10(self):
        # Title used by Gradescope 
        """HW4C - Contents of 'output_files/election_results.txt' """

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW4C"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        # Check if "output_files/election_results.txt" file is generated
        file_path = "/autograder/source/output_files/election_results.txt"
        file_generated = os.path.isfile(file_path)

        # Read the contents of output_files/election_results.txt and ref.csv
        if file_generated:
            result_content = read_file_contents(file_path)
            reference_content = read_file_contents("/autograder/source/reference/ref_election_results.txt")

            # Compare the contents
            result = compare_strings(result_content, reference_content, 5)
            print(result)

            # Standard unit test case with an associated error message
            if result_content == reference_content:
                print("\nPASSED!! Contents of 'output_files/election_results.txt' are correct.")
                self.assertTrue(True, msg="")
            else:
                print("\nFAILED!! Contents of 'output_files/election_results.txt' are incorrect.")
                self.assertTrue(False, msg="")
        else:
            # Print a message if output_files/election_results.txt is not generated
            print(f"\nFAILED!! Result file 'output_files/election_results.txt' could not be found.")
            self.assertTrue(False, msg="")
    
    # Associated point value within GradeScope
    @weight(1)
    def test11(self):
        # Title used by Gradescope 
        """HW4C - Winner"""

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW4C"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["tail", "-n", "1", "/autograder/source/reference/ref_election_IO.txt"]).decode('utf-8').strip()

        # Compare the contents
        print(f"Expected Output:\n{reference}\n")
        print(f"Your Output:\n{output.splitlines()[-1]}")

        # Standard unit test case with an associated error message
        if reference == output.splitlines()[-1]:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")

    # Associated point value within GradeScope
    @weight(2)
    def test12(self):
        # Title used by Gradescope 
        """HW4C - I/O Formatting """

        try:
            # Run the program and capture the output
            test = subprocess.run(["./HW4C"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            output = test.stdout.strip()
        except subprocess.TimeoutExpired:
            output = "Timeout expired!! Program did not exit."

        reference = subprocess.check_output(["head", "-n", "6", "/autograder/source/reference/ref_election_IO.txt"]).decode('utf-8').strip()
    
        # Compare the contents
        result = compare_strings(output, reference, 6)
        print(result)

        # Standard unit test case with an associated error message
        if reference in output:
            print("\nPASSED!!")
            self.assertTrue(True, msg="")
        else:
            print("\nFAILED!!")
            self.assertTrue(False, msg="")
        