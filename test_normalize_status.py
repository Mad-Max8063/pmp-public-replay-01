import unittest

from normalize_status import normalize_status


class NormalizeStatusTests(unittest.TestCase):
    def test_canonical_values_remain_canonical(self):
        for value in ("todo", "in-progress", "done"):
            with self.subTest(value=value):
                self.assertEqual(normalize_status(value), value)

    def test_todo_aliases(self):
        for value in ("to do", "pending"):
            with self.subTest(value=value):
                self.assertEqual(normalize_status(value), "todo")

    def test_in_progress_aliases(self):
        for value in ("in progress", "inprogress", "doing", "wip"):
            with self.subTest(value=value):
                self.assertEqual(normalize_status(value), "in-progress")

    def test_done_aliases(self):
        for value in ("complete", "completed"):
            with self.subTest(value=value):
                self.assertEqual(normalize_status(value), "done")

    def test_casefold_trim_and_separator_normalization(self):
        cases = {
            "  PENDING  ": "todo",
            "To---Do": "todo",
            "IN___PROGRESS": "in-progress",
            "  ComPLeTed ": "done",
        }
        for value, expected in cases.items():
            with self.subTest(value=value):
                self.assertEqual(normalize_status(value), expected)

    def test_empty_input_is_rejected(self):
        for value in ("", "   ", "_--_"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    ValueError, rf"^unsupported status: {value!r}$"
                ):
                    normalize_status(value)

    def test_unknown_input_is_rejected(self):
        value = "blocked"
        with self.assertRaisesRegex(ValueError, "^unsupported status: 'blocked'$"):
            normalize_status(value)


if __name__ == "__main__":
    unittest.main()
