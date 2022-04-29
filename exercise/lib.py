# install beberapa libary yang dibutuhkan terlebih dahulu
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                      'scikit-image', 'Pillow', 'imagecodecs', 'termcolor'])
