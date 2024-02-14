from setuptools import setup
import os


if os.path.isfile('requirements.txt'):
    with open('requirements.txt', 'r') as requirements_file:
        install_requires = requirements_file.read().splitlines()
for package in install_requires:
    if package.startswith('git'):
        pname = package.split('/')[-1].split('.')[0]
        install_requires[install_requires.index(package)] = pname + ' @ ' + package
setup(
    name='dataanalysis_mobilogram_conversion',
    version='0.1.0',
    url='https://github.com/gtluubruker/dataanalysis_mobilogram_conversion',
    license='Apache License',
    author='Gordon T. Luu',
    author_email='gordon.luu@bruker.com',
    packages=['bin'],
    entry_points={'console_scripts': ['convert_mobilogram=bin.run:run']},
    install_requires=install_requires
)
