from setuptools import setup, find_packages

setup(
    name='project',
    version='1.0',
    packages=find_packages(),
    install_requires=['numpy'],  # Пример зависимости
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
