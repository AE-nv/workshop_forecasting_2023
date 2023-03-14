![](docs/ae_logo.png)

# AE 2023 Workshop

Workshop for CS students

## Setup

First of all, you should have `python` and `pip` installed. You can do this in a number of ways. For mac users, [Homebrew](https://brew.sh/index_nl) is a pretty nifty package manager. The windows variant would be [Chocolatey](https://chocolatey.org). You can just go to [https://www.python.org](https://www.python.org), but where's the fun in that?

This workshop was built in `python3.9`. If you use a later version of python, you may run into trouble with some of the packages (particularly `prophet` and `pystan`.
To set up your environment, you should only have to go through the following steps.

Clone this environment (any way you want). This is how you'd do it though the terminal. First navigate to a location of your choice, then enter:

`git clone https://github.com/AE-nv/workshop_forecasting_2023.git`

This command clones a local repo onto your device. Next, you'll want to set up your environment. Create a virtual environment first:

`python3 -m venv *your_virtual_environment_name*`

Activating the virtual environment goes like this:

`source venv/bin/activate`

Then install the requirements in this environment.

`pip install -r requirements.txt`

The project makes use of jupyter notebooks. Make sure your virtual environment is registered.

`python3 -m ipykernel install --user --name=*your_virtual_environment_name*`

You can use an IDE if you want (Pycharm and VSCode have support/extensions to make that process painless), or you can run `jupyter` as a local service using

`jupyter lab`

Make sure your kernel is set to the virtual environment you created, and you should be good to go! 