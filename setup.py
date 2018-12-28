from setuptools import setup
from torch.utils.cpp_extension import CppExtension, CUDAExtension, BuildExtension

# Python interface
setup(
    name='PytorchMakefileTutorial',
    version='0.1.0',
    install_requires=['torch'],
    packages=['MakePytorchPlusPlus'],
    package_dir={'MakePytorchPlusPlus': './'},
    ext_modules=[
        CUDAExtension(
            name='MakePytorchBackend',
            include_dirs=['./'],
            sources=[
                'pybind/make_pytorch.cpp',
            ],
            libraries=['makepytorch'],
            library_dirs=['objs'],
            # extra_compile_args=['-g']
            )
    ],
    cmdclass={'build_ext': BuildExtension},
    author='Christopher B. Choy',
    author_email='chrischoy@ai.stanford.edu',
    description='Tutorial for Pytorch C++ Extension with a Makefile',
    keywords='Pytorch C++ Extension',
    url='https://github.com/chrischoy/MakePytorchPlusPlus',
    zip_safe=False,
)
