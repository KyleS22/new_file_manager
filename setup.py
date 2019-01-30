from setuptools import setup

setup(
    name='new_file_manager',
    version="1.0.0",
    packages=['new_file_manager'],
    entry_points={
        'console_scripts': ['nfm=new_file_manager.cli:main'],
    },
    description="Command line tool for creating new files with headers and templates.",
)