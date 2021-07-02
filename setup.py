from setuptools import setup

README = open('README.md', 'r').read() + '\n\n' + open('CHANGELOG.md', 'r').read()

classifiers = [
    # 'Development Status :: 1 - Beta',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    # 'Operating System :: Linux :: Dabian',
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    # 'Topic :: Encrypter And Decrypter :: Text',
]

setup(
    name="Num6",
    version="0.2",
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
