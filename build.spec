# This file is used by other spec files

import os, subprocess, sys

# Get version from git
version = subprocess.check_output(['git', 'describe', '--always', '--tags']).strip()
with open('frozenversion.py', 'w') as f:
 f.write('version = "%s"' % version)

# Generate filename
suffix = {'linux2': '-linux', 'win32': '-win', 'darwin': '-osx'}
output += '-' + version + suffix.get(sys.platform, '')

# Analyze files
a = Analysis([input], excludes=['numpy'], datas=[('certs/*', 'certs')])# Don't let comtypes include numpy
a.binaries = [((os.path.basename(name) if type == 'BINARY' else name), path, type) for name, path, type in a.binaries]# libusb binaries are not found in subdirs

# Generate executable
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas, name=output, console=console)

os.remove('frozenversion.py')
