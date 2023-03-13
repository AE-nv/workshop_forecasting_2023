![](docs/ae_logo.png)

# AE 2023 Workshop

Workshop for CS students

## Setup

First of all, you should have `python` and `pip` installed. You can do this in a number of ways. This workshop was built in `python3.9`, but we don't expect trouble with newer python versions.

To set up your environment, you should only have to go through the following steps.

Clone this environment (any way you want). This is how you'd do it though the terminal. First navigate to a location of your choice, then enter:

`git clone https://github.com/AE-nv/workshop_forecasting_2023.git`

This command clones a local repo onto your device. Next, you'll want to set up your environment. Create a virtual environment first:

`python3 -m venv *your_virtual_environment_name*`

Activating the virtual environment goes like this:

`source venv/bin/activate`

Then install the requirements in this environment.

`pip install -r requirements.txt`

The project makes use of jupyter notebooks. You can use an IDE if you want (Pycharm and VSCode have support/extensions to make that process painless), or you can run `jupyter` as a local service using

`jupyter lab`

Make sure your interpreter is set to the virtual environment you created, and you should be good to go!