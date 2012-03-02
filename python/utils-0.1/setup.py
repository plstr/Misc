from setuptools import setup, find_packages

project = 'utils'
version = 0.1

setup(name=project,
      version=version,
      description="A set of small utils I frequently use across projects",
      long_description=open('README.rst').read(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development',
      ],
      platforms='any',
      keywords='utils',
      author='Ramana',
      author_email='sramana9@gmail.com',
      url='http://bitbucket.org/sramana/utils',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      entry_points = {
          "distutils.commands": [
          "upload_sphinx = sphinx_pypi_upload:UploadDoc",
         ]
      }

     )
