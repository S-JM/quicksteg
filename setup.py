from setuptools import setup

setup(name='quicksteg',
      version='0.0.3',
      description='Quick steganography tools',
      license='GPLv3',
      classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.12',
      ],
      author='S-JM',
      url='https://github.com/s-jm/quicksteg/',
      packages=['quicksteg'],
      entry_points= {
        'console_scripts': ['quicksteg=quicksteg.quicksteg:main']
      }
     )
