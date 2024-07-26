# setup.py is used to help us to build our application as a package.

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    ---------------------------------------------------------
    this function will return the list of requirements
    ---------------------------------------------------------

    Understanding the method definition

        1) def get_requirements(file_path: str):

            This defines a function named get_requirements.
            The function takes one parameter named file_path.
            The parameter file_path is expected to be of type str (a string).

        2) -> List[str]:
            This is a return type hint.
            It indicates that the function will return a list of strings.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #replacing /n with a blank with Comprehension
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements


setup(
name = 'Student_Performance_Predictor',
version = '0.0.1',
author = 'Tarun Ramapuram',
author_email = 'tarunramapuram@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)