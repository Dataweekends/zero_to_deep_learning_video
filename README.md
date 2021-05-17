## [Check our Zero To Deep Learning 5 day bootcamp. New dates are out!](https://www.zerotodeeplearning.com/?utm_source=github.com&utm_medium=affiliate&utm_campaign=https%3A%2F%2Fgithub.com%2FDataweekends%2Fzero_to_deep_learning_video&utm_content=README.md)

------

# Zero to Deep Learning® Video Course

Welcome to the Zero to Deep Learning® Video Course repository.

## Get started guide

#### Clone this repository on your local computer

```
git clone https://github.com/Dataweekends/zero_to_deep_learning_video.git
```

#### Download and Install Anaconda Python 3.7

https://www.anaconda.com/distribution/

#### Change to course folder

```
cd zero_to_deep_learning_video
```

#### Create the course environment

```
conda env create
```

wait for the environment to create.

#### Activate the environment (Mac/Linux)
```
conda activate ztdl
```

#### Activate the environment (Windows)
```
conda activate ztdl
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
conda deactivate
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

- Mac OSX Sierra 10.15.7
- Ubuntu 18.04
- Windows 10

## Running the course on Google Colaboratory with free GPU support

Google offers a free platform to run Jupyter notebooks called Google Colaboratory. You need a Gmail or Google Apps email address to use it.

Follow these steps:

1. Open your browser and go to https://colab.research.google.com/
2. Choose the **GITHUB** tab and paste the repository address: `https://github.com/Dataweekends/zero_to_deep_learning_video` in the search bar.
3. Click on the notebook you would like to run
4. Enable GPU support in the `Edit -> Notebook Settings` menu
5. Enjoy running the notebook with GPU support!
6. If the notebook loads data from the repo you will have to download the data too. Follow these steps to do that:
  1. Create a code cell at the top of the notebook
  2. Clone the repository in Colab:
  ```
  !git clone https://github.com/Dataweekends/zero_to_deep_learning_video.git
  ```
  3. Replace the `../data` path with `zero_to_deep_learning_video/data` in the cell that loads the data.
7. Enjoy!