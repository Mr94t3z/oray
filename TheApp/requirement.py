# install beberapa libary yang dibutuhkan
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                      'flask', 'flask_wtf', 'wtforms', 'Flask-SQLAlchemy'])
