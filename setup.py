import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

requirements  = [
    "paho-mqtt",
    "requests",
    "click"
]


setuptools.setup(
    name="adm-py", 
    version="0.0.1",
    author="Davide neri",
    author_email="dneri@zerynth.com",
    description="A python library for the ADM API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://repo.zerynth.com/zerynth-adm/adm-py",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points = {
        'console_scripts': ['adm-py=adm.cli.command_line:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
