from setuptools import setup, find_packages

setup(
    name="image_editor",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pillow",
    ],
    author="Aviv Illoz",
    author_email="avivilloz@gmail.com",
    description=(
        "This is a comprehensive Python package designed to simplify and "
        "streamline image editing tasks. While currently focused on image "
        "cropping, it is built with extensibility in mind, allowing for "
        "future additions of various image manipulation features."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avivilloz/image_editor",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
