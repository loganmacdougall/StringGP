from setuptools import setup, find_packages

print(find_packages())

setup(
    name="stringgp",
    version="0.1",
    description="A package for genetic programming string analysis",
    packages=find_packages(),  # Automatically find submodules
    include_package_data=True,  # Include non-code files if specified in MANIFEST.in
    install_requires=[  # List any external dependencies here
        "numpy","matplotlib","pandas", "scikit-learn"
    ],
    package_dir={"": ".."},
)