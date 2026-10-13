'''
—Agenda__
1- Set up the github {Repository}
a)new environment
b)setup.py
c)requirements.txt
2. Src folder and build the package

» create repo
» create project folder
» Open anaconda prompt/vs code
» go to Folder location >> cd "location"
» code . >> create vs code instance
» open terminal in vs code >> cmd
» create environment >> conda create -p venv (env name) python=3.10 -y
» clear screen >> cls
» activate environment >> conda activate venv/
To activate this environment, use                                                                           
>> conda activate "D:\DS Projects\Student Performance Indicator\venv"
To deactivate an active environment, use
>> conda deactivate
» git init >> initiaializing an empty git repo
» in Folder >> create README.md file
» git add README.md
» git commit -m "first commit"
» git status >> checks status
git branch -M main
» git remote add origin [repo link]
» git remote -v
» git push -u origin main
» in git repo >> create .gitignore file >> choose python >> Commit message >> commit changes
» in Folder >> create setup.py , requirements.txt
» in setup.py >> use __init__.py files of folders to know which folders are packages
» in Folder >> create src folder >> __init__.py file

__________requirements.txt__________
numpy
pandas
-e . ## automatically triggers setup.py file

_________setup.py________
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements (file_path:str)->List[str]:

## this function will return the list of requirements

requirements=[]
with open(file_path) as file_obj:
requirements=file_obj.readlines()
requirements=[req.replace("\n", "") for req in requirements]

if HYPEN_E_DOT in requirements:
requirements.remove(HYPEN_E_DOT)

return requirements

setup(
name='mlproject',
version='0.0.1',
author='Aditi Verma',
author_email='aditiverma1605@gmail.com',
packages=find_packages(),
install_requires=get_requirements ('requirements.txt')
)

» pip install -r requirements.txt >> creates a .egg-info package

» git add .
» git  status
» git commit -m "Second commit"
» git push -u origin main
'''