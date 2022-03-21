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

    def _builtin_keywords(self) -> dict:
        return {
            "date": str(datetime.now().strftime("%Y-%m-%d")),
            "time": str(datetime.now().strftime("%H-%M")),
            "year": datetime.now().year,
            "month": datetime.now().month,
            "weekday": datetime.now().date().weekday() + 1,
            "day": datetime.now().day,
            "hour": datetime.now().hour,
            "minute": datetime.now().minute,
            "second": datetime.now().second,
            "month0": datetime.now().strftime("%m"),
            "weekday0": datetime.now().date().weekday() + 1,  # identical to "weekday", but kept for consistency with naming scheme
            "day0": datetime.now().strftime("%d"),
            "hour0": datetime.now().strftime("%H"),
            "minute0": datetime.now().strftime("%M"),
            "second0":  datetime.now().strftime("%S"),
        }

    def _throw_error_on_reserved_keywords(self) -> None:
        reserved = [key for key in self._builtin_keywords()]
        for key in self._kwargs:
            if key in reserved:
                raise ValueError(f"The keyword '{key}' is reserved and not allowed in **kwargs arguments. Please choose something else.")

    def _generate_filename(self, filename: str) -> str:
        reserved = self._builtin_keywords()
        for keyword in [key for key in reserved]:
            function = reserved[keyword]
            self._add_builtin_keyword(keyword, function)
        return self._replace_keywords(filename)

    def _add_builtin_keyword(self, key: str, value: str) -> None:
        self._kwargs = {**self._kwargs, key: value}

    def _replace_keywords(self, text: str) -> str:
        for key in self._kwargs:
            value = self._kwargs[key]
            if not (isinstance(value, str) or isinstance(value, int)):
                raise TypeError(f"Keyword '{key}' is a {type(value).__name__}, but must be a str or int.")
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
