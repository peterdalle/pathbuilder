from pathlib import Path
from datetime import datetime
import os


class PathBuilder():

    def __init__(self, filename: str, **kwargs) -> None:
        """Generates directories.

        filename: filename
        **kwargs: keywors that are inserted into the filename.
        """
        self._kwargs = kwargs
        self._throw_error_on_reserved_keywords()
        self._filename = self._generate_filename(filename)

    def _throw_error_on_reserved_keywords(self) -> None:
        reserved = [
            "date", "time", "year", 
            "month", "day", "hour", "minute", "second",
            "month0", "day0", "hour0", "minute0", "second0",
        ]
        for key in self._kwargs:
            if key in reserved:
                raise ValueError(f"The keyword '{key}' is reserved and not allowed in **kwargs arguments. Please choose something else.")

    def _generate_filename(self, filename: str) -> str:
        self._add_keyword("date", str(datetime.now().strftime("%Y-%m-%d")))
        self._add_keyword("time", str(datetime.now().strftime("%H-%M")))
        self._add_keyword("year", datetime.now().year)
        self._add_keyword("month", datetime.now().month)
        self._add_keyword("day", datetime.now().day)
        self._add_keyword("hour", datetime.now().hour)
        self._add_keyword("minute", datetime.now().minute)
        self._add_keyword("second", datetime.now().second)
        self._add_keyword("month0", datetime.now().strftime("%m"))
        self._add_keyword("day0", datetime.now().strftime("%d"))
        self._add_keyword("hour0", datetime.now().strftime("%H"))
        self._add_keyword("minute0", datetime.now().strftime("%M"))
        self._add_keyword("second0", datetime.now().strftime("%S"))
        return self._replace_kwargs(filename)

    def _add_keyword(self, key: str, value: str) -> None:
        self._kwargs = {**self._kwargs, key: value}

    def _replace_kwargs(self, text: str) -> str:
        for key in self._kwargs:
            text = text.replace("{" + key + "}", str(self._kwargs[key]))
        return text

    @property
    def fullname(self) -> str:
        """Gets path and file name: `/user/path/filename.txt`"""
        return os.path.abspath(self._filename)

    @property
    def filename(self) -> str:
        """Gets file name: `filename.txt`"""
        return os.path.basename(self._filename)

    @property
    def path(self) -> str:
        """Gets path: `/user/path/`"""
        return os.path.dirname(self._filename)

    def create_directory(self) -> None:
        """Create the full path if it does not exist."""
        Path(self.path).mkdir(parents=True, exist_ok=True)
