from setuptools import setup

setup(
    name='zetteltools',
    version='',
    packages=['zetteltools'],
    install_requires=[
        'parse',
    ],
    entry_points={
        'console_scripts': [
            'zk=zetteltools.main:main',
        ],
    },
    url='https://github.com/nelsonlove/zettel-tools',
    license='',
    author='Nelson Love',
    author_email='',
    description=''
)
