from distutils.core import setup

setup(
  name = 'yacp',
  packages = ['yacp'],
  version = '0.1',
  license='MIT',
  description = 'Yet Another Crawler Package. A simple directory crawler. You can use it by a generator or by creating an instance',
  long_description="A directory crawler based on generators. Using generators slow down the process a bit, but fixes memory issues with that way you can crawl into large files",
  author = 'Ada BERK',
  author_email = 'adaberk.kth@gmail.com',
  url='https://github.com/visualcoders/YACP',
  download_url='https://github.com/visualcoders/YACP/archive/v0.1.tar.gz',
  keywords = ['Crawling', 'Directory', 'Library', 'Package', 'Simple', 'Generator', 'Context Manager', 'Variable', 'Helper'],  
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
