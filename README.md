# AppearOnline

![GitHub last commit](https://img.shields.io/github/last-commit/gansel51/appear-online)
![visitors](https://pageview.vercel.app/?github_user=gansel51)
![maintained](https://img.shields.io/maintenance/yes/2021)
![maintainer](https://img.shields.io/badge/Maintainer-gansel51-informational)

The appear online repository is a usable script to run when you step away from your computer. From going to the bathroom to running errands, there are many reason why people may step away from their computer but don't want their computer to turn off. Appear Online simulates mouse movement and keyboard usage to keep your computer appearing active!

## Supported Operating Systens

At this time, AppearOnline is only available to Windows and Linux users. MacOS is not supported in the beta version.

## Installation

Installation is available via releases or by cloning the project using the command `git clone https://github.com/gansel51/appear-online.git`.

## Requirements

The requirements for use are included in the `requirements.txt` file. The command `pip install -r requirements.txt` from the root of the project will install all necessary python libraries in the current environment.

_Warning: the current dependencies are not building properly, so AppearOnline will not function as anticipated._

## Use

_This project is still being completed and is not available for stable use._

Once this project is installed locally, navegate to the root of the project and use the command line `python controller.py --runtime X`, where `X` is the intended runtime. The runtime command line argument is optional, and the time will default to 5 hours if not specified.
