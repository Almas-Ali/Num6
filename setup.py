from setuptools import setup

README = open('README.md', 'r').read() + '\n\n' + open('CHANGELOG.txt', 'r').read()

classifiers = [
    "Development status :: In Beta version/Stable",
    "Operating system :: All Python supported devices.",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="Num6",
    version="0.1",
    description="This is a Python 3 based Encrypter and Decrypter tool (open source).",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/almas-ali/num6",
    author="Md. Almas Ali",
    author_email="almaspr3@gmail.com",
    keyword="Encrypter, Decrypter, Num6",
    license="MIT",
    classifiers=classifiers,
    packages=['num6'],
    install_requires=[],
)
