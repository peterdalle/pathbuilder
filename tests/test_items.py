# -*- coding: utf-8 -*-
import os
import random
import string
import unittest
from urllib.parse import urljoin
from pathbuilder import PathBuilder
from datetime import datetime
import tempfile


class Test_PathBuilder(unittest.TestCase):

    def test_default(self):
        db = PathBuilder("/users/path/filename.json")
        self.assertEqual(db.filename, "filename.json")
        self.assertEqual(db.path, "/users/path")
        self.assertEqual(db.fullname, "C:\\users\path\\filename.json")

    def test_builtin_keywords(self):
        db = PathBuilder("/users/{year}/{month}/{day}/filename.json")
        yyyy = datetime.now().year
        mm = datetime.now().month
        dd = datetime.now().day
        self.assertEqual(db.filename, "filename.json")
        self.assertEqual(db.path, f"/users/{yyyy}/{mm}/{dd}")
        self.assertEqual(db.fullname, f"C:\\users\\{yyyy}\\{mm}\\{dd}\\filename.json")

    def test_custom_keywords(self):
        db = PathBuilder("/users/{custom}/filename.json", custom="hello-world")
        self.assertEqual(db.filename, "filename.json")
        self.assertEqual(db.path, "/users/hello-world")
        self.assertEqual(db.fullname, f"C:\\users\\hello-world\\filename.json")
    
    def test_override_builtin_keywords(self):
        self.assertRaises(ValueError, PathBuilder, filename="/users/{year}/filename.json", year="2000")

    def test_create_directory_and_put_file_inside(self):
        path = tempfile.gettempdir() + "\\{year}-{project}\\"
        file = self._generate_random_text(30) + ".tmp"
        fullname = path + file
        db = PathBuilder(fullname, project="test")
        db.create_directory()
        with open(db.fullname, "w") as f:
            f.write("Hello World")
        os.remove(db.fullname)

    def _generate_random_text(self, n: int):
        return "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))
 

if __name__ == '__main__':
    pass #unittest.main()
