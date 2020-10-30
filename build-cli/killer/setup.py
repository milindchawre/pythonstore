from setuptools import setup, find_packages

with open("README.md", encoding="UTF-8") as f:
    readme = f.read()

setup(
    name="killer",
    version="0.1.0",
    description="CLI utility for killing processes listening of specific port.",
    long_description=readme,
    author="Milind",
    author_email="example@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "killer=killer.cli:main",
        ],
    },
)
