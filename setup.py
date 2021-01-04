import setuptools

with open("README.md") as readme:
    long_description = readme.read()

setuptools.setup(
    name="hypixelaPY",
    version="1.0.0",
    author="myerfire",
    author_email="realmyerfire@gmail.com",
    description="An API wrapper for the Hypixel API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myerfire/hypixelaPY",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
