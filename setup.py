from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='d5mit_learn_maths',
      version='0.3',
      description='Test',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['d5mit_learn_maths'],
      zip_safe=False)

