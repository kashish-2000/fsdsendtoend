from setuptools import find_packages,setup

setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='kashish gupta',
    author_email='kashishguptaagrawal@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)