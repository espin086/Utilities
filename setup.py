from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="jjutils",
    version="0.0.9",
    packages=find_packages(),
    install_requires=requirements,
)
