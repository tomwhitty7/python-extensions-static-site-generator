import sys
import importlib
from pathlib import Path

def load_module(directory, name):
    sys.path[0].insert(directory)

def load_directory(directory):
    for
