from distutils.core import setup
import py2exe

setup(console=[{ "script": "bundlefiles0_test.py"}],
    options={"py2exe": {
        "bundle_files": 0,
        "excludes": "tkinter",
        "verbose": 4}},
     zipfile=None)
