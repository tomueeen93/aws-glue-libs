from setuptools import find_packages, setup

setup(
    name='awsglue',
    version='2.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
