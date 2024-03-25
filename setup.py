from setuptools import setup, find_packages

setup(
    name='mkparse',
    version='0.3.2',
    description="A simple Makefile Parser written in Python that is designed to simplify the process of importing Makefile contents into python as dictionary (key-value mappings (i.e. hashmap/associative arrays)) objects",
    author='Thanatisia',
    author_email='55834101+Thanatisia@users.noreply.github.com',
    # packages=["mkparse"] ,# Default: find_packages()
    # package_dir={'mkparse':'src'},
    package_dir={"": "src"},
    install_requires=[
        # List your dependencies here
    ],
    url='https://github.com/Thanatisia/makefile-parser-python',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)

