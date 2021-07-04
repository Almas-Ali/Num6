# Num6 - A Powerful Encrypter And Decrypter Tool
**Version 0.2**

Num6 is a very intelligent and efficient encrypter and decrypter open source tool. 
It is very fast and mostly user friendly.
Every characters are very much efficiently added to the library.
There just imaginary numbers not copied from anything.
All numbers are 6 digit number, this how it named **Num6**.
It is a Command Line Tools Upcoming is **GUI** Coming Soon...

**This is a Python 3 based script. Made and developed by [Md. Almas Ali](https://facebook.com/md.almasali.0 "Md. Almas Ali")**

[![license](https://img.shields.io/github/license/dwisiswant0/WiFiID.svg "LICENSE")](LICENSE)

![GitHub repo size](https://img.shields.io/github/repo-size/Almas-Ali/Num6?style=plastic "Size")

## Logo
![Image](IMG/logo0.jpg)

## Character Library
![Image](IMG/img1.png)
![Image](IMG/img2.png)
![Image](IMG/img3.png)
![Image](IMG/img4.png)
![Image](IMG/img5.png)

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
num6.encrypt('This is a test string', 2)
```
**Output**
```
112112112212112112112212112112112212112212333133112212333133112212333133112212112212333133333133112212112212333133333133211222211222333133333133333133333133333133333133122111333133112212112212333133333133112212112212333133333133211222211222333133333133333133333133333133333133122111333133122111333133122111333133122111333133333133333133333133333133122111333133333133211222211222333133211222333133122111122111333133333133122111122111333133333133211222211222333133333133333133211222211222333133211222333133333133333133333133333133122111333133333133333133211222211222333133333133333133211222211222333133211222333133333133211222211222333133211222211222112212112212333133333133112212112212211222333133333133333133211222211222122111122111333133333133122111333133
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
num6.decrypt('112112112212112112112212112112112212112212333133112212333133112212333133112212112212333133333133112212112212333133333133211222211222333133333133333133333133333133333133122111333133112212112212333133333133112212112212333133333133211222211222333133333133333133333133333133333133122111333133122111333133122111333133122111333133333133333133333133333133122111333133333133211222211222333133211222333133122111122111333133333133122111122111333133333133211222211222333133333133333133211222211222333133211222333133333133333133333133333133122111333133333133333133211222211222333133333133333133211222211222333133211222333133333133211222211222333133211222211222112212112212333133333133112212112212211222333133333133333133211222211222122111122111333133333133122111333133', 2)
```
**Output**
```
This is a test string
```

## External Use
You can also use it as a CLI.
#### Windows
```
python -m num6
```
#### Linux
```
python3 -m num6
```

## Encode your scripts
You can encode your scripts using this num6 module like builtin module marshal and base64 in Python3. Many fetures you can compare. Give it try today ! 
<br>


## For any bug report feel free to set a pull request or issue in Github

Our Github link : [Num6][3] <br>
Pypi link : [Num6][4] <br>

[1]: <https://git-scm.com/download> "Git"
[2]: <https://python.org/downloads> "Python 3"
[3]: <https://github.com/almas-ali/num6> "Num6 Github"
[4]: <https://pypi.org/project/Num6> "Num6 Pypi"

-----------------------
Change Logs
========================

1. Initial relese 0.0.1 (18-11-2020)

2. Updated some feture and made it comfurtable for python internal use. 0.1 (11-04-2021)

3. Updated some codes, improved performance, minor bugfix. 0.2 (02-07-2021)

4. Minor changed to functions. (04-07-2021)
    1. Functions name changed.
        1. encrypter() to encrypt()
        2. decrypter() to decrypt()
    
    2. Now those function will can take two argumens.
        1. **Strings** : Which is encryption or decryption values.
        2. **Pin** : Which is security number for encryption or decryption values. It can be must than 6 For some issue. It wll increase soon.
    3. Logics chaged. It is not so huge difference so on. But we are trying to improve our logics.

--------------------------