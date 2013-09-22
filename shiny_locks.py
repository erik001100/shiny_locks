#!/usr/bin/env python

import os, sys
from contextlib import contextmanager

@contextmanager
def file_lock(lock_file):
    if os.path.exists(lock_file):
        print("Only one script can run at once. Script is locked with {0}"
                .format(lock_file))
        sys.exit(-1)
    else:
        open(lock_file, 'w').write("1")
        try:
            yield
        finally:
            os.remove(lock_file)
