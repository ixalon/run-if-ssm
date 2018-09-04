from setuptools import setup
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name="run-if-ssm",
	version="1.0.0",
	author="Chris Warren",
	author_email="chris@ixalon.com",
	description=("A command line utility for running commands if a AWS SSM parameter is set."),
	license="BSD",
	keywords="aws",
	url="https://github.com/ixalon/run-if-ssm",
	install_requires=[
		'boto3',
		'argh',
	],
	scripts=['bin/run-if-ssm'],
	long_description=read('README.md'),
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"License :: OSI Approved :: BSD License",
	],
)
