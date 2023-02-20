"Install all required libraries"

from setuptools import find_packages, setup
from typing import List


REQUIREMENTS_FILE = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements()->List[str]:
    "Fetch all the libraries from requirements file"
    with open(REQUIREMENTS_FILE) as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [requirement.replace("\n", "") for requirement in requirements_list]

        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT) 

    return requirements_list


setup(
    name="System Monitor",
    version="0.0.1",
    author="Abhijeet Srivastav",
    author_email="abhijeetsrivastav292@gmail.com",
    description="System monitoring app",
    license="MIT License",
    packages=find_packages(),
    install_requires=get_requirements()
)