import unittest
import module_12_1
import module_12_2
import test_12_3

runnerTest = unittest.TestSuite()

runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)


runner.run(runnerTest)

