from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if '-e .' in requirments:
            requirments.remove('-e .')

    return requirments

setup(
    name="Student-performance-prediction",
    version="0.0.1",
    author="Aman",
    author_email="mramn4887@gmail.com",
    packages = find_packages(),
    install_requires= get_requirements('requirements.txt')

    )