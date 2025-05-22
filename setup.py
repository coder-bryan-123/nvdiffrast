# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

import nvdiffrast
import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

def is_rocm_backend():
    if os.getenv('ROCM_HOME') or os.path.exists('/opt/rocm'):
        return True
    else:
        return False
    
def get_package_data():
    package_data = {}
    if is_rocm_backend():
        source_files = [
            'common/*.h',
            'common/*.inl',
            'common/*.hip',
            'common/*.cpp',
            'common/hipraster/*.hpp',
            'common/hipraster/impl/*.cpp',
            'common/hipraster/impl/*.hpp',
            'common/hipraster/impl/*.inl',
            'common/hipraster/impl/*.hip',
            'lib/*.h',
            'torch/*.h',
            'torch/*.inl',
            'torch/*.cpp',
            'tensorflow/*.hip',
        ]
    else:
        source_files = [
            'common/*.h',
            'common/*.inl',
            'common/*.cu',
            'common/*.cpp',
            'common/cudaraster/*.hpp',
            'common/cudaraster/impl/*.cpp',
            'common/cudaraster/impl/*.hpp',
            'common/cudaraster/impl/*.inl',
            'common/cudaraster/impl/*.cu',
            'lib/*.h',
            'torch/*.h',
            'torch/*.inl',
            'torch/*.cpp',
            'tensorflow/*.cu',
        ]
    if os.name == "nt":
        source_files += ['lib/*.lib']
    package_data['nvdiffrast'] = source_files

    return package_data

setuptools.setup(
    name="nvdiffrast",
    version=nvdiffrast.__version__,
    author="Samuli Laine",
    author_email="slaine@nvidia.com",
    description="nvdiffrast - modular primitives for high-performance differentiable rendering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NVlabs/nvdiffrast",
    packages=setuptools.find_packages(),
    package_data=get_package_data(),
    include_package_data=True,
    install_requires=['numpy'],  # note: can't require torch here as it will install torch even for a TensorFlow container
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
