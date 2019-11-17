import os.path
import sys
newPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
sys.path.append(newPath)
from app import app
sys.path.remove(newPath)
del newPath
