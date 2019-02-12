import setuptools
from version import __version__

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="foxylib",
    version=__version__,
    description="First package",
    author="Moonyoung Kang",
    author_email="yerihyo@gmail.com",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/foxytrixy-com/foxylib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)