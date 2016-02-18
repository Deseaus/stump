from setuptools import find_packages
from setuptools import setup

from XXX import version

setup(
    name="XXX",
    version=version,
    description="",
    author="Daniel Vidal Hussey",
    author_email="vidal@ferret-go.com",
    maintainer="Daniel Vidal Hussey",
    maintainer_email="vidal@ferret-go.com",
    url="",
    namespace_packages=[""],
    packages=find_packages(),
    extras_require=dict(
        test=[
            "test",
        ]
    ),
    install_requires=[
        "package",
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "script = path.to.module:method",
        ]
    }
)
