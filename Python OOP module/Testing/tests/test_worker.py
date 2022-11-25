import unittest


from Testing.codes.worker import Worker


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Pesho", 1000, 100)

    def test_correct_initialization(self):
        self.assertEqual("Pesho", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_working_when_no_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_working_when_worker_has_energy(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)
        self.assertEqual(99, self.worker.energy)

    def test_resting(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_info_method(self):
        self.assertEqual('Pesho has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    unittest.main()
