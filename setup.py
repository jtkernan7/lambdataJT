import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdatajtk",
    version="0.0.1",
    author="John Timothy Kernan Jr",
    author_email="jtkernan7@gmail.com",
    description="simple helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtkernan7/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module1-python-modules-packages-and-environments",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
