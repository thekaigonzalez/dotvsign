import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vsign-vsi-kai-gonzalez",
    version="1.0.0",
    author="Kai D. Gonzalez",
    author_email="gkai70264@gmail.com",
    description="A simple library for comparing versions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thekaigonzalez/dotvsign",
    project_urls={
        "Bug Tracker": "https://github.com/thekaigonzalez/dotvsign/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "vsign"},
    packages=setuptools.find_packages(where="vsign"),
    python_requires=">=3.6",
)