import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):

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

    def test_usain_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.first, self.third)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(results.keys())].name == self.third)

    def test_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[max(results.keys())].name == self.third)

    def test_usain_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.first, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(results[max(results.keys())].name == self.third)


if __name__ == '__main__':
    unittest.main()
