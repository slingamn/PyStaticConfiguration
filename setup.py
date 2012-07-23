try:
    from setuptools import setup
    assert setup
except ImportError:
    from distutils.core import setup

setup(
    name="PyStaticConfiguration",
    version="0.1",
    provides=["staticconf"],
    author="Daniel Nephin",
    author_email="dnephin@gmail.com",
    url="http://github.com/dnephin/PyStaticConfiguration",
    description='A python library for loading static configuration',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
    ],
    packages=['staticconf'],
)