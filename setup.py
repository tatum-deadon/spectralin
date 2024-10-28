from setuptools import setup, find_packages

setup(
    name="spectralin",
    version="0.1.0",
    author="Tatum Deadon",
    description="Static analysis and code quality scanner",
    packages=find_packages(),
    python_requires=">=3.9",
    extras_require={"dev": ["pytest>=7.0"]},
    entry_points={"console_scripts": ["spectralin=spectralin.__main__:main"]},
)
