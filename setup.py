from setuptools import setup

setup(
    name='passgen',
    version='0.1',
    py_modules=['passgen'],
    entry_points={
        'console_scripts': [
            'passgen=passgen:main',
        ],
    },
)
