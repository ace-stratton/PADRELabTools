import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setuptools.setup(
    name="operations-framework",
    version="0.4.7",
    description="EnduroSat operations framework.",
    url="https://gitlab.endurosatlab.com/cloud-segment/cdgs/operations-framework",
    author="EnduroSat",
    author_email="support@endurosat.com",
    packages=setuptools.find_packages(),
    py_modules=["operations", "util", "cfg.access_cfg", "cfg.defaults_cfg"],
    python_requires=">=3.8",
    install_requires=["requests", "python-dateutil", "six"],
    long_description="Project used to automate spacecraft operations at EnduroSat.",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
