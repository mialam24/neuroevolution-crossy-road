from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('process_image_crossy_road_cy.pyx'))

# python3 setup.py build_ext --inplace
