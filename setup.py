from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'   # there is direct relation between setup.py and requirements.txt

def get_requirements(file_path:str)->List[str]:  # here we will give a file name and in return we will get list
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements.txt:
            requirements.remove(HYPEN_E_DOT)




        return requirements


setup(
        name = 'DiamondPricePrediction',
        version='0.0.1',
        author ='Krish',
        author_email='akashkikani7039@gmail.com',
        install_requries = get_requirements('requirements.txt'),
        packages=find_packages()




)