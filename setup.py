from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirement_file:
    requirements_list = requirement_file.readlines()
    requirements_list = [lib.replace("\n", "") for lib in requirements_list]

requirements = requirements_list

setup(
    name='Causal-Inference',
    version="0.1.0",
    description="",
    url='https://github.com/DiyeMark/Causal-Inference',
    author="Diye Mark",
    author_email="diyye101@gmail.com",
    license="MIT License",
    install_requires=requirements,
    long_description=readme,
)
