import os

def get_parent_path(path):
    """Get parent directory of a path"""
    return os.path.dirname(path)

def join_paths(base, *paths):
    """Join multiple path components"""
    return os.path.join(base, *paths)

def get_basename(path):
    """Get base name of a path"""
    return os.path.basename(path)