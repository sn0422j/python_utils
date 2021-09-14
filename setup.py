from setuptools import setup, find_packages

setup(
    name="python_utils",
    version="0.1.0",
    description="Python Utilities",
    author="sn0422j",
    packages=find_packages("python_utils"),
    package_dir={"": "python_utils"},
    python_requires=">=3.7",
)
