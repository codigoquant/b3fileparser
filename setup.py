from setuptools import setup, find_packages


setup(
    name='b3fileparser',
    version='0.1.3.11',
    description='A Python parser of B3 historical files.',
    url='https://github.com/codigoquant/b3fileparser',
    author='codigoquant',
    author_email='codigoquant@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['pandas>=1.3.0']
)
