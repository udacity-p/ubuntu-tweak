import glob
from setuptools import *

setup(name='ubuntu-tweak',
      version='0.4.999.20091125',
      description='magic tool to configure Ubuntu',
      author='TualatriX',  
      author_email='tualatrix@gmail.com',
      url='http://ubuntu-tweak.com',
      scripts=['ubuntu-tweak'],
      packages=[
          'ubuntutweak',
          'ubuntutweak.conf',
          'ubuntutweak.common',
          'ubuntutweak.backends',
          'ubuntutweak.network',
          'ubuntutweak.policykit',
          'ubuntutweak.widgets',
          'ubuntutweak.modules',
          'ubuntutweak.utils',
      ],
      data_files=[
          ('../etc/dbus-1/system.d/', ['data/ubuntu-tweak-daemon.conf']),
          ('share/dbus-1/system-services', ['data/com.ubuntu_tweak.daemon.service']),
          ('share/ubuntu-tweak/applogos/', glob.glob('data/applogos/*.png')),
          ('share/ubuntu-tweak/ui/', glob.glob('data/ui/*.ui')),
          ('share/ubuntu-tweak/pixmaps/', glob.glob('data/pixmaps/*.png')),
          ('share/ubuntu-tweak/status/', glob.glob('data/status/*.png')),
          ('share/ubuntu-tweak/', ['data/keys.xml']),
          ('share/ubuntu-tweak/', ['data/ubuntu-tweak-daemon']),
          ],
      license='GNU GPL',
      platforms='linux',
)
