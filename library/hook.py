import importlib.util
import sys
from pathlib import Path


def importPy(name):
    libPATH = Path(__file__).parent / f'{name}.py'
    spec = importlib.util.spec_from_file_location(f"library.{name}", str(libPATH))
    lib = importlib.util.module_from_spec(spec)
    sys.modules[f"library.{name}"] = lib
    spec.loader.exec_module(lib)
    
    return lib

def main():
    
    window=importPy('window')
    window.run()