# PathBuilder: package to generate and create paths

PathBuilder is a small Python package that generates a path and creates the physical folder directory using keywords in the path.

For example, `/path/{year}/file.txt` translates into `/path/2022/file.txt`. 

You can also add your own keywords.

## Install

<!--
```bash
pip install pathbuilder
```
-->

Development version:

```bash
pip install git+https://github.com/peterdalle/pathbuilder.git@v0.9.1
```

## Example

```py
from pathbuilder import PathBuilder

db = PathBuilder("/path/{year}/file.txt")

print(db.fullname)  # /path/2022/file.txt
print(db.path)      # /path/2022
print(db.filename)  # file.txt

# Creates /path/2022 if it does not exist
db.create_directory()
```

## Example with keywords

The keyword `{project}` below is replaced with the keyword arguments ([**kwargs](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)) with the same name.

```py
from pathbuilder import pathbuilder

db = PathBuilder("/Downloads/{project}/{year}.txt", project="alpha")

print(db.fullname)  # /Downloads/alpha/2022.txt
print(db.path)      # /Downloads/alpha
print(db.filename)  # 2022.txt

db.create_directory()
```

## Documentation

There are a number of common built-in keywords for date and time that works out of the box.

Date/time keyword | Translates into
---- | --------------
`{date}` | Date in `yyyy-mm-dd` format (e.g. 2022-01-25)
`{time}` | Time in `HH-MM` format in 24 hours clock (e.g. 23-44)
`{year}` | Year in `yyyy` format
`{month}` | Month 1-12
`{day}` | Day 1-31
`{hour}` | Hour 0-23
`{minute}` | Minute 0-59
`{second}` | Second 0-59
`{month0}` | Month with zero padding (01-12)
`{day0}` | Day with zero padding (01-31)
`{hour0}` | Hour with zero padding (00-23)
`{minute0}` | Minute with zero padding (00-59)
`{second0}` | Second with zero padding (00-59)

## Support

[Create a new issue](https://github.com/peterdalle/pathbuilder/issues)

## License

[MIT](LICENSE)