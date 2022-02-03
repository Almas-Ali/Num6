import setuptools

with open('README.md', 'r') as README:
    long_description = README.read()

classifiers = [
    'Development Status :: 4 - Beta',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    'Topic :: Security :: Cryptography',
    'Natural Language :: English',
    'Environment :: Console',
]

setuptools.setup(
    name="Num6",
    version="0.4.0",
    description="Num6 - An cryptography tool for Python 3 (open source).",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/almas-ali/num6",
    author="Md. Almas Ali",
    author_email="almaspr3@gmail.com",
    keyword="Encrypter, Decrypter, Num6",
    license="MIT",
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points='''
        [console_scripts]
        num6=num6.cli:main_cli
    '''
)
