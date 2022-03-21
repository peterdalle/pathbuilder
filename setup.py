from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    description = fh.read()
  
setup(
    name="pathbuilder",
    version="0.9.3",
    author="Peter M. Dahlgren",
    author_email="peterdalle@gmail.com",
    packages=find_packages(),
    description="Generates or creates a path folder directory using keywords in the path",
    keywords=['python', 'path', 'folder', 'directory'],
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/peterdale/pathbuilder",
    license='MIT',
    python_requires='>=3.7',
    install_requires=[],
    classifiers= [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ]
)