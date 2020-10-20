from setuptools import setup

setup(
    name='hacktoberfest_jems',
    author='Tiffany Souterre',
    version='1.0.1',
    packages=['hacktoberfest_jems'],
    description="An application to celebrate hacktoberfest!",
    include_package_data=True,
    entry_points={
        'console_scripts': ['hacktoberfest_jems=hacktoberfest_jems.main:main']
    }
)