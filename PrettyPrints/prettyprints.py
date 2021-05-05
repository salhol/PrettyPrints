## Python 3.9
## By: Sally Holm
from os import get_terminal_size
import subprocess

def TW():
    """
    Use to get terminal window width.

    Returns:
        int: Current terminal width
    """
    TERMINALWIDTH = get_terminal_size()
    return TERMINALWIDTH.columns

def Dashed(TW=TW()):
    """Print a spacing bar made from "-".

    Args:
        TW (int, optional): Specify spacing width. Defaults to TW().
    """
    print('-'*TW)

def Dotted(TW=TW()):
    """Print a spacing bar made from ".".

    Args:
        TW (int, optional): Specify spacing width. Defaults to TW().
    """
    print('.'*TW)

def Equal(TW=TW()):
    """Print a spacing bar made from "=".

    Args:
        TW (int, optional): Specify spacing width. Defaults to TW().
    """
    print('='*TW)

def Squared(TW=TW()):
    """Print a spacing bar made from "#".

    Args:
        TW (int, optional): Specify spacing width. Defaults to TW().
    """
    print('#'*TW)

def Spacing(symbol='X', TW=TW()):
    """Print a spacing bar from given symbol.

    Args:
        symbol (str, optional): Specify symbol to use as spacing bar. Defaults to 'X'.
        TW (int, optional): Specify spacing width. Defaults to TW().
    """
    print(symbol*TW)

def Centered(string, symbol="", TW=TW()):
    """Print centered text string.

    Args:
        string (str): String to be centered.
        symbol (str, optional): Symbol to use to center with. Defaults to whitespace.
        TW (int, optional): Specify center width. Defaults to TW().
    """
    print(f"{string:{symbol}^{TW}}")
