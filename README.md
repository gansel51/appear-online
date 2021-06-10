<img width="281" alt="available" src="https://user-images.githubusercontent.com/59709552/121570145-96d76f80-c9ef-11eb-8e09-76e0983f7af8.png">

# AppearOnline

![GitHub last commit](https://img.shields.io/github/last-commit/gansel51/appear-online)
![maintained](https://img.shields.io/maintenance/yes/2021)
![maintainer](https://img.shields.io/badge/Maintainer-gansel51-informational)

The AppearOnline project is intended to be run when you step away from your computer. From going to the bathroom to running errands, there are many reason why people may step away from their computer but don't want their computer to turn off or show that they are away. AppearOnline simulates mouse movement and keyboard usage to keep your computer appearing active! Users of Microsoft Teams will appear available while this program is running.

## Installation

Installation is available via GitHub releases or by cloning the project using the command `git clone https://github.com/gansel51/appear-online.git`.

## Requirements

### Windows or Linux

The requirements for use are included in the `requirements.txt` file. The command `pip install -r requirements.txt` from the root of the project will install all necessary python libraries in the current environment.

### MacOS

The requirements for use are included in the `mac-requirements.txt` file. MacOS users may need to install each requirement in the specified order using the command `pip install X`, where `X` is the requirement. Finding a workaround to improve ease of use on MacOS is high priority for the project maintainers.

During the first run of this project, MacOS users may be prompted to allow accesibility access to their IDE or terminal. For this project to work, accessibility must be granted.


## Use

_This project has released a beta version but is still actively being improved._

Once this project is installed locally, navegate to the root of the project and use the command line `python controller.py --runtime X`, where `X` is the intended runtime (in minutes). The runtime command line argument is optional, and the time will default to one hour if not specified.

## License

This project is made available under the MIT license. No warranty is provided for users of this product, nor are the authors liable for any issues arising from the use of this project. See the license for more information and fair usage information.
