# PathBuilder: package to generate and create paths

PathBuilder is a small Python package that generates a path and creates the physical folder directory using keywords in the path.

For example, `/path/{year}/report.txt` translates into `/path/2022/report.txt`. 

You can also add your own keywords.

## Install

<!--
```bash
pip install pathbuilder
```
-->

Development version:

```bash
pip install git+https://github.com/peterdalle/pathbuilder.git@v0.9.3
```

## Example

```py
from pathbuilder import PathBuilder

pb = PathBuilder("/path/{year}/report.txt")

print(pb.fullname)  # /path/2022/report.txt
print(pb.path)      # /path/2022
print(pb.filename)  # report.txt

# Creates /path/2022 if it does not exist
pb.create_directory()
```

## Example with keywords

The keyword `{project}` below is replaced with the keyword arguments ([**kwargs](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)) with the same name.

```py
from pathbuilder import PathBuilder

pb = PathBuilder("/company/{project}/{year}.txt", project="alpha")

print(pb.fullname)  # /company/alpha/2022.txt
print(pb.path)      # /company/alpha
print(pb.filename)  # 2022.txt

pb.create_directory()
```

## Documentation

There are a number of common built-in keywords for date and time that works out of the box.

Date/time keyword | Translates into
---- | --------------
`{date}` | Date in `yyyy-mm-dd` format (e.g. 2022-01-25)
`{time}` | Time in `HH-MM` format in 24 hours clock (e.g. 23-44)
`{year}` | Year in `yyyy` format
`{month}` | Month 1-12
`{weekday}` | Weekday 1-7 (1=Monday to 7=Sunday)
`{day}` | Day 1-31
`{hour}` | Hour 0-23
`{minute}` | Minute 0-59
`{second}` | Second 0-59
`{month0}` | Month with zero padding (01-12)
`{weekday0}` | Weekday with zero padding (01-07)
`{day0}` | Day with zero padding (01-31)
`{hour0}` | Hour with zero padding (00-23)
`{minute0}` | Minute with zero padding (00-59)
`{second0}` | Second with zero padding (00-59)

## Support

[Create a new issue](https://github.com/peterdalle/pathbuilder/issues)

## License

[MIT](LICENSE)