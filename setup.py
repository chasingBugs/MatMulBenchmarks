# python setup.py develop
from Cython.Build import cythonize
from setuptools import Extension, setup

DISTNAME = 'matmulmethods'
AUTHOR = 'Maximilian Hengstmann'
AUTHOR_EMAIL = 'maxi.hengstmann@web.de'
DESCRIPTION = ' MatMul methods for benchmarking'
LICENSE = 'MIT'
README = 'MatMul methods for benchmarking'

INSTALL_REQUIRES = [
    'numpy',
    'Cython'
]

CYTHON_EXTENSION = [
    Extension(
        name='cython_methods',
        sources=['cython_methods.pyx']
    )
]

EXT_MODULES = cythonize(CYTHON_EXTENSION)

metadata = dict(
    name=DISTNAME,
    long_description=README,
    ext_modules=EXT_MODULES,
    install_requires=INSTALL_REQUIRES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE
)


def setup_package() -> None:
    setup(**metadata)


if __name__ == '__main__':
    setup_package()
