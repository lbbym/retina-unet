from setuptools import setup
from setuptools import find_packages

setup(name='retina-unet',
      version='0.0.1',
      description='kjads',
      author='Alejandro Valdes',
      url='https://github.com/alevalv/retina-unet',
      download_url='https://github.com/alevalv/retina-unet/archive/master.zip',
      license='MIT',
      install_requires=['Keras>=2.0.8', 'opencv-python>=2.4.10', 'h5py'],
      packages=find_packages())
