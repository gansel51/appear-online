import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="appearonline",
    version="1.0.0",
    description="Appear Online in Microsoft Teams",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gansel51/appear-online",
    author="Griffin Ansel",
    author_email="griffin.ansel@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["appear_online"],
    include_package_data=True,
    install_requires=["pyobjc-framework-Quartz==7.3",
                      'mouse==0.7.1 ; platform_system=="Windows"',
                      'mouse==0.7.1 ; platform_system=="Linux"',
                      'macmouse==0.7.3 ; platform_system=="Darwin"'],
    entry_points={
        "console_scripts": [
            "appearonline=appear_online.__main__:main",
        ]
    },
)