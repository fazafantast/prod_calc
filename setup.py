import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prodcalc",
    version="0.3b",
    packages=setuptools.find_packages(),
    description="Производственный календарь(РФ)",
    long_description=long_description,
    author="Alexandr Faizullin",
    author_email="faizullin.fan@gmail.com",
    maintainer="Alexandr Faizullin",
    maintainer_email="faizullin.fan@gmail.com",
    url="https://github.com/fazafantast/prod_calc",
    license="Apache 2.0",
    classifiers=["Development Status :: 4 - Beta",
                 "Environment :: Console",
                 "License :: Freeware",
                 "License :: OSI Approved :: Apache Software License",
                 "Natural Language :: Russia",
                 "Programming Language :: Python :: 3.6",
                 "Topic :: Utilities"],
    python_requires=">=3.6",
    package_data={"prodcalc": ["data/prod_calc.csv"]},
)
