from distutils.core import setup
setup(
  name = 'david_to_entrez_converter',
  packages = ['david_to_entrez_converter'],
  version = '0.1',
  license='MIT',
  description = 'Convert the HGNC gene names to ENTREZ id available in the DAVID bioinformatics database.',
  author = 'Benjamin Pham',
  author_email = 'bkpham@ucsd.edu',
  url = 'https://github.com/user/b-k-pham',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['DAVID','Gene','Conversion'],
  install_requires=[
          'pandas',
          'numpy',
          'os'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)