from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rwave',
    packages=['rwave'],
    install_requires=["numpy", "scipy", "librosa"],

    version='0.1.1',
    license='MIT',

    author='Tatsuya Abe',
    author_email='abe12@mccc.jp',

    url='https://github.com/AjxLab/RWave',

    desription='A utility that handle audio for Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='audio wave wav convert mfcc fft fs',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
