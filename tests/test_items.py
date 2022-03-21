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

    def test_properties_works(self):
        db = PathBuilder("/users/path/filename.json")
        self.assertEqual(db.filename, "filename.json")
        self.assertEqual(db.path, "/users/path")
        self.assertEqual(db.fullname, "C:\\users\path\\filename.json")

    def test_builtin_keywords_Works(self):
        db = PathBuilder("/users/{year}/{month}/{day}/{hour}/{minute}/{date}/{weekday}/filename.json")
        date = datetime.now().date()
        yyyy = datetime.now().year
        weekday = datetime.now().date().weekday() + 1
        mm = datetime.now().month
        dd = datetime.now().day
        HH = datetime.now().hour
        MM = datetime.now().minute
        self.assertEqual(db.filename, "filename.json")
        self.assertEqual(db.path, f"/users/{yyyy}/{mm}/{dd}/{HH}/{MM}/{date}/{weekday}")
        self.assertEqual(db.fullname, f"C:\\users\\{yyyy}\\{mm}\\{dd}\\{HH}\\{MM}\\{date}\\{weekday}\\filename.json")

    def test_custom_keywords_works(self):
        db = PathBuilder("/users/{foo}/{bar}/filename.json", foo="hello", bar="world")
        self.assertEqual(db.filename, "filename.json")
        self.assertEqual(db.path, "/users/hello/world")
        self.assertEqual(db.fullname, f"C:\\users\\hello\\world\\filename.json")

    def test_quirky_custom_keywords_works(self):
        db1 = PathBuilder("/users/filename.json", not_used="2000")
        db2 = PathBuilder("/{used}/filename.json", used=200, not_used=404)
        self.assertEqual(db1.filename, "filename.json")
        self.assertEqual(db2.path, "/200")

    def test_incorrect_argument_types_doesnt_work(self):
        self.assertRaises(TypeError, PathBuilder, filename="{dict}/file.json", dict={"foo": "bar"})
        self.assertRaises(TypeError, PathBuilder, filename="{list}/file.json", list=[200])
        self.assertRaises(TypeError, PathBuilder, filename="{func}/file.json", func=datetime.now)

    def test_override_builtin_keywords_fails(self):
        self.assertRaises(ValueError, PathBuilder, filename="/users/{year}/file.json", year="2000")

    def test_create_directory_and_put_file_inside_works(self):
        path = tempfile.gettempdir() + "\\{year}-{project}\\"
        file = self._generate_random_text(30) + ".tmp"
        fullname = path + file
        db = PathBuilder(fullname, project="test")
        db.create_directory()
        with open(db.fullname, "w") as f:
            f.write("Hello World")
        with open(db.fullname, "r") as f:
            text = f.readline()
        os.remove(db.fullname)
        self.assertEqual(text, "Hello World")

    def _generate_random_text(self, n: int):
        return "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))
 

if __name__ == '__main__':
    pass #unittest.main()
