import runner
import unittest


class RunnerTest(unittest.TestCase):
    distance = 0

    def test_run(self):
        for i in range(10):
            self.distance += runner.Runner('Turtle').run()
        self.assertEqual(self.distance, 100)

    def test_walk(self):
        for i in range(10):
            self.distance += runner.Runner('Rabbit').walk()
        self.assertEqual(self.distance, 50)

    def test_chalenge(self):
        first = runner.Runner('Turtle')
        second = runner.Runner('Rabbit')
        for i in range(10):
            self.distance = self.test_run
            self.distance = self.test_walk
        self.assertNotEqual(first, second)


if __name__ == '__main__':
    unittest.main()


