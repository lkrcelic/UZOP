from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize(Extension(
        "string_kernel",
        sources=["string_kernel.pyx"],
        include_dirs=[numpy.get_include()],  # Add this line
    )),
)
