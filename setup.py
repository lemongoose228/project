from setuptools import setup, find_packages

setup(
    name='project',
    version='1.0',
     packages=find_packages(exclude=['test']),
    install_requires=['numpy'],  
    author='Kate Konova',
    author_email='konova.ek@mail.ru',
    description='calculates the area of ​​a circle given a given radius and is used to check if a number is prime',
    url='https://github.com/lemongoose228/project.git',
    extras_require={
          'test': [
              'pytest',
              'coverage',
          ],
     },
    license='MIT',
)
