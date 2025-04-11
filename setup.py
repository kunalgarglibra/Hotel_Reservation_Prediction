from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name= "ML_OPS_P1",
    version= "0.1",
    author= "Kunal",
    packages= find_packages(),
    install_requires = requirements,
    
)