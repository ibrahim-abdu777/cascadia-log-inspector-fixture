import unittest

from src.log_inspector import count_levels


class CountLevelsTests(unittest.TestCase):
    def test_counts_levels_case_insensitively(self):
        self.assertEqual(
            count_levels(["INFO started", "error failed", "INFO stopped"]),
            {"INFO": 2, "ERROR": 1},
        )

    def test_ignores_blank_and_unknown_lines(self):
        self.assertEqual(count_levels(["", "hello", " WARNING slow "]), {"WARNING": 1})


if __name__ == "__main__":
    unittest.main()
