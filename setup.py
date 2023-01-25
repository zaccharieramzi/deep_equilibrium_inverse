import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# taken from https://github.com/CEA-COSMIC/ModOpt/blob/master/setup.py
with open('requirements.txt') as open_file:
    install_requires = open_file.read()

setuptools.setup(
    name="deep-equilibrium-inverse",
    version="0.0.1",
    author="Davis Gilton",
    author_email="davislgilton@gmail.com",
    description="DEQs for inverse problems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dgilton/deep_equilibrium_inverse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    extras_require={
        'test': ['pytest'],
    },
    python_requires='>=3.6',
)