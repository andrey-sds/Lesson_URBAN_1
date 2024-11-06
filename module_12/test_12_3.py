import runner
import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):
    distance = 0
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        for i in range(10):
            self.distance += runner.Runner('Turtle').run()
        self.assertEqual(self.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        for i in range(10):
            self.distance += runner.Runner('Rabbit').walk()
        self.assertEqual(self.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_chalenge(self):
        first = runner.Runner('Turtle')
        second = runner.Runner('Rabbit')
        for i in range(10):
            self.distance = self.test_run
            self.distance = self.test_walk
        self.assertNotEqual(first, second)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.first = runner_and_tournament.Runner('Андрей', 9)
        self.second = runner_and_tournament.Runner('Усейн', 10)
        self.third = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results):
            result = cls.all_results[key]
            named_result = {pos: runner.name for pos, runner in result.items()}
            print(f"{key}: {named_result}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_usain_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.first, self.third)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(results.keys())].name == self.third)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[max(results.keys())].name == self.third)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # @unittest.skipIf(test_andrey_and_nick, "Не нужен")
    def test_usain_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.first, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(results[max(results.keys())].name == self.third)


if __name__ == '__main__':
    unittest.main()
