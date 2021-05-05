# PrettyPrints

> A must-have for all lazy python enthusiasts who wants pretty prints in the terminal window!

Is what I would like to say, but to be real, I am probably the only one who gets annoyed at ugly prints from my python script when I resize my terminal window.   

**This python package is 100% more work than what is worth.**
---
## Installation
- Install with pip
```
pip install git+https://github.com/salhol/prettyprints.git#egg=PrettyPrints
```
- Install with setup.py
```
cd C:\Users\user\Downloads\PrettyPrints\
setup.py install
```
- Install with pip from PyPi
```
pip install PrettyPrints
```

## Features

- Print spacings that will always be the same width as your terminal window
- Print centered text
- Bragging rights to your friends that you wasted time on this

## How to use

```python
from PrettyPrints import *
print(TW())
Dashed()
Dotted()
Equal()
Squared()
Spacing()
Spacing("*")
Centered("Text to center")
Centered("Text to center with dots",".")
```
![Screenshot of example](https://github.com/salhol/PrettyPrints/blob/main/Example.png)
*Please note that I suck at coding, therefore, continue at your own risk.*
