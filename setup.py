from setuptools import setup, find_packages

setup(
    name='pp-commit',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pp_commit = pp_commit:main'
        ]
    }
)
