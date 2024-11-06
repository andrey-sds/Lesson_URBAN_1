from module_12 import rt_with_exceptions
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    distance = 0

    def test_run(self):
        try:
            rt_with_exceptions.Runner('Rabbit', -9).run()
            logging.info("'test_run' выполнен успешно")
            self.distance = rt_with_exceptions.Runner('Rabbit', -9).run()
            return self.distance
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            return -1

    def test_walk(self):
        try:
            rt_with_exceptions.Runner(100, 10).walk()
            logging.info("'test_walk' выполнен успешно")
            self.distance = rt_with_exceptions.Runner(100, 10).walk()
            return self.distance
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return -1


if __name__ == '__main__':
    unittest.main()

