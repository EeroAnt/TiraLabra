import os

def _locate_message(name):
    return os.path.exists(f"src/Viestit/{name}.txt")

def _locate_key(name):
    return os.path.exists(f"src/Avaimet/{name}_private")