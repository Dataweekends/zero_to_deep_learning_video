# Zero to Deep Learning™ Udemy Video Course


Welcome to the Zero to Deep Learning Video Course repository

## Get started guide

#### Clone this repository on your local computer

```
git clone https://github.com/Dataweekends/zero_to_deep_learning_udemy.git
```

#### Download and Install Anaconda Python 3.6

https://www.continuum.io/downloads

#### Change to course folder

```
cd zero_to_deep_learning_udemy
```

#### Create the course environment

```
conda env create
```

wait for the environment to create.

#### Activate the environment (Mac/Linux)
```
source activate ztdl
```

#### Activate the environment (Windows)
```
activate ztdl
```

Check that your prompt changed to

```
(ztdl) $
```

#### Launch Jupyter Notebook

```
jupyter notebook
```

#### Open your browser to

```
http://localhost:8888
```

#### Run the Check environment Notebook

Go to the course folder, open the notebook `0_Check_Environment.ipynb` and run it. If you see the message:

    Houston we are go!

You are good to go! Enjoy!


#### Troubleshooting installation
If for some reason you don't see `Houston we are go!`, the simplest solution is to delete the environment and start from scratch again.

To remove the environment:

- close the browser and go back to your terminal
- stop jupyter notebook (CTRL-C)
- deactivate the environment (Mac/Linux):

```
source deactivate
```

- deactivate the environment (Windows 10):

```
deactivate ztdl
```

- delete the environment:

```
conda remove -y -n ztdl --all
```

- restart from environment creation and make sure that each steps completes till the end.

#### Updating Conda

One thing you can also try is to update your conda executable. This may help if you already had Anaconda installed on your system.

```
conda update conda
```

These instructions have been tested on:

- Mac OSX Sierra 10.12.4
- Ubuntu 16.04
- Windows 10

## Running the course on Floyd with GPU support

The guys at [FloydHub](www.floydhub.com) are doing an excellent job of providing a zero-install platform-as-a-service for training and deploying DL models in the cloud. Here are the steps to run the course on Floyd:

#### Sign-up on FloydHub

Go to: www.floydhub.com and register. As a new user you get 100 hours of free GPU, which is a great starting point.

#### Install or update Floyd

In the terminal, with the activated `ztdl` environment, run:
```
pip install -U floyd-cli
```

#### Login into Floyd
```
floyd login
```
This will open a browser and you will have to log in with your User/Password. Then copy the token to the terminal and hit ENTER.

#### Initialize the current project
```
floyd init zerotodeeplearning
```

#### Run a notebook with GPU support
```
floyd run --mode jupyter --env tensorflow --gpu --data rz8m3aPaKt95PDTdEa4U6N
```
Wait for the notebook to come online and then navigate to the url

#### Enjoy GPU power
Run a notebook and experience the awesome power of a GPU!

#### STOP floyd
When you are finished, remember to STOP the floyd environment so that you don't incur in charges.
```
floyd stop <PROJECT-ID>
```
Make sure that you have stopped the project by checking the floyd page.

