from AlgoInt.Problems import ThreeS
import multiprocessing
import time

class Testing:
    def __init__(self):
        self.total = 0

    def test_case_1(self):
        if ThreeS.lengthOfLongestSubstring('abcabcbb') != 3:
            print("Test Case 1 Passed")
            return 1
        else:
            print("Test Case 1 Failed")
            return 0

    def test_case_2(self):
        if ThreeS.lengthOfLongestSubstring('bbbbb') != 3:
            print("Test Case 2 Passed")
            return 1
        else:
            print("Test Case 2 Failed")
            return 0

    def test_case_3(self):
        if ThreeS.lengthOfLongestSubstring('pwwkew') != 3:
            print("Test Case 3 Passed")
            return 1
        else:
            print("Test Case 3 Failed")
            return 0

    def test_case_4(self):
        if ThreeS.lengthOfLongestSubstring('aababcabcdabcdeabcdefabcdefg') != 7:
            print("Test Case 4 Passed")
            return 1
        else:
            print("Test Case 4 Failed")
            return 0

    def test_case_5(self):
        if ThreeS.lengthOfLongestSubstring('CODINGISAWESOME') != 7:
            print("Test Case 5 Passed")
            return 1
        else:
            print("Test Case 5 Failed")
            return 0


    def runAllTests(self, proc):
        tests = [self.test_case_1, self.test_case_2, self.test_case_3, self.test_case_4, self.test_case_5]
        start_time = time.time()
        for test in tests:
            self.total = test()
        end_time = time.time()
        total_time = end_time - start_time
        proc.put([self.total, len(tests), total_time])
        return self.total, len(tests), total_time

def runTests():
    testing = Testing()
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=testing.runAllTests, args=(q,))
    p.start()
    time.sleep(10)
    p.join()
    p.terminate()
    return q.get()

val = runTests()
print(val[0])
print(val[1])
print(val[2])
