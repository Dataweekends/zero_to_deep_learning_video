# tests that too long to execute on Travis are temporarily commented out
# TODO: find a way to fix this

import subprocess
import tempfile


def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test_0():
    _exec_notebook('course/0_Check_Environment.ipynb')


def test_1():
    _exec_notebook('course/1 First Deep Learning Model.ipynb')


def test_2():
    _exec_notebook('course/2 Data.ipynb')


def test_3():
    _exec_notebook('course/3 Machine Learning.ipynb')


def test_4():
    _exec_notebook('course/4 Deep Learning Intro.ipynb')


def test_5():
    _exec_notebook('course/5 Gradient Descent.ipynb')


def test_6():
    _exec_notebook('course/6 Convolutional Neural Networks.ipynb')


def test_8():
    _exec_notebook('course/8 Recurrent Neural Networks.ipynb')


def test_9():
    _exec_notebook('course/9 Improving performance.ipynb')


def test_2_sol():
    _exec_notebook('solutions/2 Data exploration Exercises Solution.ipynb')


def test_3_sol():
    _exec_notebook('solutions/3 Machine Learning Exercises Solution.ipynb')


def test_4_sol():
    _exec_notebook('solutions/4 Deep Learning Intro Exercises Solution.ipynb')


def test_5_sol():
    _exec_notebook('solutions/5 Gradient Descent Exercises Solution.ipynb')


def test_6_sol():
    _exec_notebook('solutions/6 Convolutional Neural Networks Exercises Solution.ipynb')


def test_8_sol():
    _exec_notebook('solutions/8 Recurrent Neural Networks Exercises Solutions.ipynb')


def test_9_sol():
    _exec_notebook('solutions/9 Improving performance Exercises Solutions.ipynb')
