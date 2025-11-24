from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="upas-ia",
    version="3.1.0",
    author="Thomas Calvet",
    author_email="thomascalvet@humanologic.com",
    description="Unified Protocol for Auditable Scientific AI Assistance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/humanologue/UPAS-IA-FRAMEWORK",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[],
)