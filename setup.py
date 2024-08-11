from setuptools import find_packages, setup

setup(
    name='nikilib',
    packages=find_packages(include=['nikilib']),
    version='0.0.1',
    description='My first Python library',
    author='Niki Crow',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)