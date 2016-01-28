from setuptools import find_packages
from setuptools import setup

from XXX import version

setup(
    name="XXX",
    version=version,
    description="",
    author="",
    author_email="",
    maintainer="",
    maintainer_email="",
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
