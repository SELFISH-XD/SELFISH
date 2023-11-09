import os, sys
try:
    __import__("selfishr").SELFISH()
except Exception as e:
    exit(str(e))
