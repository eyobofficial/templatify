from setuptools import setup

setup(
    name='templatify',
    version='0.1.0',
    py_modules=['templatify'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'templatify = templatify:cli',
        ],
    },
)