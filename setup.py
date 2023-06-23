from setuptools import setup

def README() -> str:
    with open("README.md", "rt") as text:
        return text.read()

setup(
    name="pyenum",
    version="0.0.0",
    description="Better enums",
    long_description=README(),
    author="Marcos Delay",
    author_email="dev.marcosdly@gmail.com",
    url="https://github.com/marcosdly/pyenum",
    package_dir={"pyenum": "src"},
    packages=["pyenum"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities"
    ],
    license="GPL-2.0",
    keywords=["enum", "rust", "better", "enums"],
    platforms=["py3-none-any"],
    requires=[],
    python_requires=">=3.7.0"
)