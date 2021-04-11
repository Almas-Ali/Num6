from setuptools import setup

setup(
    name="Num6",
    version="0.1",
    description="This is a Python 3 based Encrypter and Decrypter tool (open source).",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url="https://github.com/almas-ali/num6",
    author="Md. Almas Ali",
    author_email="almaspr3@gmail.com",
    keyword="Encrypter, Decrypter, Num6",
    license="MIT",
    classifiers=[
        "Development status :: In Beta version/Stable",
        "Operating system :: All Python supported devices.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=['num6'],
    install_requires=[],
)
