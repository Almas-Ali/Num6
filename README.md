# Num6 - A Powerful Cryptography Tool
**Version 0.4.0**

### Breef Introduction:

Num6 is a very intelligent and efficient cryptography open source utility. 
It is very fast and mostly user friendly.
Every characters are very much efficiently added to the library.
There just imaginary numbers not copied from anything.
All numbers are 6 digit number, this how it named **Num6**.



### **Latest Num6 GUI** : <a href="#num6-gui" title="Num6 GUI">Learn from here</a>

**This is a Python 3 based script. Made and developed by [Md. Almas Ali][6]**

> Jump to latest changes <a href="#latest" title="Latest Change">Latest Chages</a>

### Details
[![LICENSE](https://img.shields.io/github/license/dwisiswant0/WiFiID.svg "LICENSE")](LICENSE)
![GitHub repo size](https://img.shields.io/github/repo-size/Almas-Ali/Num6?style=plastic "Size")

### Downloads
[![Downloads](https://static.pepy.tech/personalized-badge/num6?period=total&units=none&left_color=grey&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/num6 "Downloads")

> To get more details about this project download visit [Num6 Downloads][5]


## Logo
![Image](https://raw.githubusercontent.com/Almas-Ali/Num6/main/IMG/logo0.jpg)

## Character Library
![Image](https://raw.githubusercontent.com/Almas-Ali/Num6/main/IMG/img1.png)
![Image](https://raw.githubusercontent.com/Almas-Ali/Num6/main/IMG/img2.png)
![Image](https://raw.githubusercontent.com/Almas-Ali/Num6/main/IMG/img3.png)
![Image](https://raw.githubusercontent.com/Almas-Ali/Num6/main/IMG/img4.png)
![Image](https://raw.githubusercontent.com/Almas-Ali/Num6/main/IMG/img5.png)

## **Installation:**
As this is a python package, so you will have to setup this tool by pip.

## **For Windows**
Install Python 3 then follow the steps.
```
pip install num6
```

## **For Linux**
### All steps are given below: <br>
First install some essentials <br>
```
sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python3 python3-dev python3-pip
```
Now you can install Num6 by pip.
```
pip3 install num6
```

## Installing from source
If your qurious you can also install it from source. For that you need this github repository in your computer. <br>
To clone this repository past this command in your command prompt or terminal. <br>

1. First install git

    1. For windows :
        * Download it from [Git][1] website.

    2. For Linux :
        ```
        sudo apt-get install git
        ```
2. Then past this command in your prompt:
    
    ```
    git clone https://github.com/almas-ali/num6.git
    ```
3. After clonning this repository follow this steps:

    1. For windows :

        1. Download [Git][1] from website.
        2. Download [Python 3][2] from website.
        3. Type `cd Num6`
        4. Type `python setup.py install`

    2. For Linux :

        1. First install [Git][1]
            ```
            sudo apt-get install git
            ```
        2. Then install [Python 3][2]
            ```
            sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python3 python3-dev python3-pip
            ```

        3. After install [Python 3][2]
            * Type `cd Num6`
            * Type `python3 setup.py install`

## **Usage**
After you have successfully install Num6 on your system, then you can import it.
```
import num6
```
You can use two magor functions in there encrypt() and decrypt(). They takes two arguments now, string and pin. String is must but pin is optional. As default pin is 1.

**Example**

```
import num6
num6.encrypt('This is a test string')
```
**Output**
```
525252202020220022003300000010220022003300000010101010000010033030110011003300033030000010003300033030033033220022300033110010
```

```
import num6
num6.encrypt('This is a test string', 59)
```
**Output**
```
100000101010100000033002200220100000033002200220202022525250003220022330330030330003300010000030330003300110011030330001001133
```
Now how can you decrypt it like ugly looking number.

**Example**
```
import num6
num6.decrypt('525252202020220022003300000010220022003300000010101010000010033030110011003300033030000010003300033030033033220022300033110010')
```

**Output**
```
This is a test string
```

**Second example**
```
import num6
num6.decrypt('100000101010100000033002200220100000033002200220202022525250003220022330330030330003300010000030330003300110011030330001001133', 59)
```
**Output**
```
This is a test string
```

<div id="cli-example"></div>

## External Use As CLI
You can also use it as a CLI.
#### Windows
```
num6 -h
```
#### Linux
```
num6 -h
```

#### Output
```
usage: Num6 [-h] [-v] [-e ENCRYPT] [-d DECRYPT] [-p PIN] [-c] [-g]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show the version information
  -e ENCRYPT, --encrypt ENCRYPT
                        to encrypt data from cli
  -d DECRYPT, --decrypt DECRYPT
                        to decrypt data from cli
  -p PIN, --pin PIN     set pin for encrpyt or decrypt data from cli
  -c, --cli             to use in interactive cli mode
  -g, --gui             to use in interactive GUI mode

```

## Some commands that you have to know

### In line encryption and decryption

### Encryption
#### Input (without any pin spacified)
```
num6 -e 'test string'
```

#### Output
```
033030110011003300033030000010003300033030033033220022300033110010
```

#### Input (with pin spacified)

```
num6 -e 'Num6 is great !' -p 34
```

### Output

```
002201000033133100022200444442422401110011330330010011010000003300221221120100000303300101
```


### decryption
#### Input (without any pin spacified)
```
num6 -d 033030110011003300033030000010003300033030033033220022300033110010
```

#### Output
```
test string
```

#### Input (with pin spacified)

```
num6 -d 002201000033133100022200444442422401110011330330010011010000003300221221120100000303300101 -p 34
```

### Output

```
Num6 is great !
```

### Calling the interactive CLI tool
```
num6 --cli
```
**CLI Interface**

```
Num6 - A Powerful Cryptography Tool

1.  For word or line encryption
2.  For word or line decryption

3.  For file encryption enter path
4.  For file decryption enter path

0.  For stop the programme
00. For clearing the screen

© Copyright collected by Md. Almas Ali

Choice : 
```

We don't need to teach it to you. Anyone can play with it and learn it. It's an user friendly tool for our users.

<div id="num6-gui"></div>

## *Introducenig Num6 GUI*

A GUI tool for Num6 package. Now you can use it more easily than never before ! It's now in on alpha development. Keep supporting us for future new features. <br>

Type `num6 -g` or `num6 --gui` to access alpha realese of Num6 GUI.

## Encode your scripts
You can encode your scripts using this num6 module like builtin module marshal and base64 in Python3. Many fetures you can compare. Give it try today ! 
<br>


## For any bug report feel free to set a pull request or issue in Github

Create A Issue: [Here][7] <br>
Make Pull Request: [Here][8] <br>
<br>
Our Github link : [Num6][3] <br>
Pypi link : [Num6][4] <br>

[1]: <https://git-scm.com/download> "Git"
[2]: <https://python.org/downloads> "Python 3"
[3]: <https://github.com/almas-ali/num6> "Num6 Github"
[4]: <https://pypi.org/project/Num6> "Num6 Pypi"
[5]: <https://pepy.tech/project/num6> "Download History"
[6]: <https://facebook.com/md.almasali.0> "Md. Almas Ali"
[7]: <https://github.com/almas-ali/num6/issues/new> "Create A Issue"
[8]: <https://github.com/almas-ali/num6/pulls> "Make Pull Request"

-----------------------

Change Logs
========================

> Jump to latest changes <a href="#latest" title="Latest Change">Latest Chage</a>

1. Initial relese 0.0.1 (18-11-2020)

2. Updated some feture and made it comfurtable for python internal use. 0.1 (11-04-2021)

3. Updated some codes, improved performance, minor bugfix. 0.2 (02-07-2021)

4. Minor changed to functions. 0.3 (04-07-2021)
    1. Functions name changed.
        1. encrypter() to encrypt()
        2. decrypter() to decrypt()
    
    2. Now those function will can take two argumens.
        1. **Strings** : Which is encryption or decryption values.
        2. **Pin** : Which is security number for encryption or decryption values. It can be must than 6 For some issue. It wll increase soon.
    3. Logics chaged. It is not so huge difference so on. But we are trying to improve our logics.


5. Documentation update and minor bug fixed. 0.3.1 (04-07-2021)
    1. In this version of [Num6][3] We have clear some documentation.
    2. Interactive CLI have been added. <a href="#cli-example" title="CLI Example">CLI Example</a>


6. Important bugfix on programe. 0.3.2 (23-09-2021)
    1. When import it starts cli mode automatically. Now it fixed.
    2. Changed privet keys to privet.

7. Major bugfix case was failing the hole programe. (10-12-2021)
    1. Changed charlib merged into packages for solving problem.
    2. Introducing Num6 GUI Alpha development realese. <a href="#num6-gui" title="Num6 GUI">Num6 GUI</a>


<div id="latest"></div>

8. Major speed improvement ! (04-02-2022)
    1. Speed up all functions (encrypt, decrypt). No late on execution.
    2. Pin setup limitation fixed.

--------------------------
