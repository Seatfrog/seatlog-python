import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seatlog",
    version="1.0.0",
    author="Seatfrog",
    author_email="dirks@seatfrog.com",
    description="Small logging package for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Seatfrog/seatlog-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["python-json-logger"]
)

