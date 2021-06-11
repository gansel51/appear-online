<img width="281" alt="available" src="https://user-images.githubusercontent.com/59709552/121570145-96d76f80-c9ef-11eb-8e09-76e0983f7af8.png">

# AppearOnline
![version](https://img.shields.io/pypi/v/AppearOnline)
![maintained](https://img.shields.io/maintenance/yes/2021)
![GitHub last commit](https://img.shields.io/github/last-commit/gansel51/appear-online)
![maintainer](https://img.shields.io/badge/Maintainer-gansel51-informational)

The AppearOnline project is intended to be run when you step away from your computer. From going to the bathroom to running errands, there are many reason why people may step away from their computer but don't want their computer to turn off or show that they are away. AppearOnline simulates mouse movement and keyboard usage to keep your computer appearing active! Users of Microsoft Teams will appear available while this program is running.

## Installation

### PyPi

Installation is available via PyPi using `pip install appearonline`.

### GitHub

Installation is available via GitHub releases or by cloning the project using the command `git clone https://github.com/gansel51/appear-online.git`.

## Requirements

Users should install the requirements by installing their operating system's `requirements.txt` file. This can be done via the command `pip install -r mac-requirements.txt`. Supported operating systems are MacOS, Windows, and Linux.
### MacOS Security and Privacy Settings

MacOS users may initially be prompted to allow accesibility access to their IDE or terminal. For this project to work, accessibility must be granted. To do so, go to System Preferences -> Security & Privacy -> Accessibility and add the IDE or terminal you are using to run the program. This will only need to be done once per application used.

## Use

If installed from PyPi, use the command `appearonline --runtime X` where `X` is the number of minutes fir the program to run. This parameter is optional, and will default to 60 minutes if not specified.

To quit the package, use the keyboard interrupt of `ctrl + c`.

Like this project? [Show your support!](https://www.buymeacoffee.com/gansel51)
## License

This project is made available under the MIT license. No warranty is provided for users of this product, nor are the authors liable for any issues arising from the use of this project. See the license for more information and fair usage information.
