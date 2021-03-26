import setuptools
from foxylib.version import __version__

# with open("README.md", "r") as fh:
#     long_description = fh.read()

install_requires = [
    "future==0.17.1",
    "nose==1.3.7",
    "pyyaml==5.4",
    "python-dateutil==2.8.0",
    "Jinja2==2.10.1",
    "ply==3.11",

    "uritemplate==3.0.0",

    "pytz==2019.3",
    "requests==2.22.0",
    "elasticsearch==7.0.1",
    "beautifulsoup4==4.7.1",
    "frozendict==1.2",
    "dill==0.3.0",
    "pymongo==3.8.0",
    "pytz==2019.3",
    "iso3166==1.0",
    "pytest==5.2.2",
    "PyGithub==1.44.1",
]


setuptools.setup(
    name="foxylib",
    version=__version__,
    description=("First package"),
    author="Moonyoung Kang",
    author_email="yerihyo@gmail.com",
    long_description="foxylib",
    #long_description_content_type="text/markdown",
    url="https://github.com/foxytrixy-com/foxylib",
    install_requires=install_requires,

    packages=setuptools.find_namespace_packages(exclude=["scripts*","venv*"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
