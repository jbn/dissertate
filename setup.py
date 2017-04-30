from setuptools import setup, find_packages


setup(
    name='dissertate',
    version='0.0.1',
    description="A package and CLI for writing dissertations",
    long_description="See: `github repo <https://github.com/jbn/dissertate>`_.",
    url="https://github.com/jbn/dissertate",
    author="John Bjorn Nelson",
    author_email="jbn@pathdependent.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords=["phd", "dissertation", "thesis", "jupyter", "ipython"],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
)
