![](docs/ae_logo.png)

# AE 2023 Workshop

Workshop for CS students.

## Part 1 - Data engineering

## Part 2 - Data science

There's two ways of approaching this segment. If you want to be more hands-on, you can set up a local environment and go through the steps listed under [Local setup](#local-setup). In case of trouble, or if you just want to take the easy road (boo), go to the [Colab links](#colab).

### Local setup

#### 1. Mac

First of all, you should have `python` and `pip` installed. You can do this in a number of ways. For mac users, [Homebrew](https://brew.sh/index_nl) is a pretty nifty package manager. The windows variant would be [Chocolatey](https://chocolatey.org). You can just go to [https://www.python.org](https://www.python.org), but where's the fun in that?

This workshop was built in `python3.9`. If you use a later version of python, you may run into trouble with some of the packages (particularly `prophet` and `pystan`).
To set up your environment, you should only have to go through the following steps.

Clone this environment (any way you want). This is how you'd do it though the terminal. First navigate to a location of your choice, then enter:

> `$ git clone https://github.com/AE-nv/workshop_forecasting_2023.git`

This command clones a local repo onto your device. Make sure to navigate to the folder you just created. It should be called **workshop\_forecasting\_2023**. Next, you'll want to set up your environment. Create a virtual environment first:

> `$ python3.9 -m venv ae_ws_env`

Note that you can use `python` or `python3` instead of `python3.9`, as long as they point to the correct version of python (3.9). You can find this out by typing `which python`, for instance, which shows you the path with which this command is associated.

Activating the virtual environment goes like this:

> `$ source ae_ws_env/bin/activate`

You can check whether the `python` command now points to your virtual environment by using `which python` or `which python3` again. Now install the requirements in this environment.

> `$ pip install -r requirements.txt`

The project makes use of jupyter notebooks. Make sure your virtual environment is registered.

> `$ python3 -m ipykernel install --user --name=ae_ws_env`

You can use an IDE if you want (Pycharm and VSCode have support/extensions to make that process 'painless'), or you can run `jupyter` as a local service using

> `$ jupyter lab`

If you get an error message about not finding the kernel, don't worry about that. Just make sure your kernel is set to the virtual environment you created (**ae\_ws\_env**), and you should be good to go! The notebooks are in a separate folder. Find them and go to the first notebook: [1_EDA-student.ipynb](notebooks/1_EDA-student.ipynb). Afterwards, you can go to the second notebook: [2\_forecasting\_mlflow-student.ipynb](notebooks/2_forecasting_mlflow-student.ipynb). 

In the second of these notebooks, you should be able to visit the `mlflow ui` using that very command. **Don't terminate the jupyter server!** Open a new terminal window, and make sure to navigate to your project directory. Then source your virtual environment (see above), as this is where mlflow was installed. As you go through the notebook, you'll see the list of runs fill up, and you can play around with visualizing the results. Don't forget to make the metrics columns visible (top right).


#### 2. Windows

The approach for Windows is very similar, but a little more convoluted (because Windows).

Open CMD as admin, and enter the following command to install chocolatey (another package manager):

> `$ @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`

Check if it works with:

> `$ choco -?`

Now check your python version: 

> `$ python –version` (or python3 –version)

If the version does not match 3.9, enter: 

> `$ choco install python –version=3.9`

Now run commands with `py -3.9 X`.

To create a virtual environment, go to the folder where you want to clone the repository, and type:

> `$ py -3.9 -m venv ae_ws_env`

This creates your virtual environment, which you can activate by calling

>`$ ae_ws_env/Scripts/activate`

The other steps mimick the ones described in the mac section: 

1. clone the repo with the git command
2. cd into the newly created folder
3. pip install the requirements
4. register the kernel

🚀 Good to go!

### Colab

If the steps above fail, or you're lazy, you can try the links below to find the same notebooks hosted on colab. Note that MLFlow won't work, here.

<font color='red'>**Duplicate the notebooks first!**</font>

#### Student versions
1. EDA - [link](https://colab.research.google.com/drive/1y34B94m17Xg4Gn4lHMepq7V6FmVrvKuo?usp=sharing)
2. Forecasting - [link](https://colab.research.google.com/drive/11NLtb9YinaDa0VqVQ8wxpaYGbl8J1ouG?usp=sharing)


#### Reference versions
1. EDA - [link](https://colab.research.google.com/drive/1cLdW2mW2vxnp3Lmp16MNvPdVCXYDly3t?usp=sharing)
2. Forecasting - [link](https://colab.research.google.com/drive/1ePpDxz2FgaxRTTBD2OecAa1NWdrJBTvx?usp=sharing)