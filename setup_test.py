from setuptools import setup

setup(
   name='ipatool',
   version='1.0',
   description='download ipa easily',
   author='NyaMisty',
   author_email='nyamisty@users.noreply.github.com',
   packages=['ipatool'],  #same as name
   install_requires=['rich', 'requests'], #external packages as dependencies
)
