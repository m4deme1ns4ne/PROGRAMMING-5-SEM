from setuptools import setup

setup(
    name='printHelloWorld',
    version='0.1',
    py_modules=['printHelloWorld'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'print-hello=printHelloWorld:main',
        ],
    },
)
