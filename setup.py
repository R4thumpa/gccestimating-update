from setuptools import setup

setup(
    name="gccestimating",
    version="0.2.0",
    author="Siegfried Gündert",
    author_email="siegfried.guendert@gmail.com",
    license="MPL-2.0",
    py_modules=["gccestimating"],
    extras_require={"numpy": ["numpy"]},
)
