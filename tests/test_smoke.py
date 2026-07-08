from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from repair_desk.cli import main
from repair_desk.models import Note, ProjectState, Task


class ProjectSmokeTests(unittest.TestCase):
    def test_cli_help(self) -> None:
        self.assertEqual(main([]), 0)


if __name__ == "__main__":
    unittest.main()
