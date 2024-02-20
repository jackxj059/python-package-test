from setuptools import setup, find_packages

setup(
    name='example',
    version='0.1',
    packages=find_packages(),  # 自動找到所有的package
    author='Jack',
    author_email='jackdyworking@example.com',
    description='A simple example package',
    long_description='A longer description of your package',
    url='https://github.com/jackxj059/python-package-test',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
