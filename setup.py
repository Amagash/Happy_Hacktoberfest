from setuptools import setup

setup(
    name='hacktoberfest_jems',
    author='Tiffany Souterre',
    version='1.0.0',
    packages=['hacktoberfest_jems'],
    description="An application to celebrate hacktoberfest!",
    entry_points={
        'console_scripts': ['hacktoberfest_jems=hacktoberfest_jems.main:main']
    }
)