import subprocess
import tempfile


def _notebook_run(path):
    """Execute a notebook via nbconvert"""
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test_0():
    _notebook_run('course/0_Check_Environment.ipynb')


def test_1():
    _notebook_run('course/1 First Deep Learning Model.ipynb')


def test_2():
    _notebook_run('course/2 Data.ipynb')


def test_3():
    _notebook_run('course/3 Machine Learning.ipynb')


def test_4():
    _notebook_run('course/4 Deep Learning Intro.ipynb')


def test_5():
    _notebook_run('course/5 Gradient Descent.ipynb')


def test_6():
    _notebook_run('course/6 Convolutional Neural Networks.ipynb')


def test_8():
    _notebook_run('course/8 Recurrent Neural Networks.ipynb')


def test_9():
    _notebook_run('course/9 Improving performance.ipynb')


def test_2_sol():
    _notebook_run('solutions/2 Data exploration Exercises Solution.ipynb')


def test_3_sol():
    _notebook_run('solutions/3 Machine Learning Exercises Solution.ipynb')


def test_4_sol():
    _notebook_run('solutions/4 Deep Learning Intro Exercises Solution.ipynb')


def test_5_sol():
    _notebook_run('solutions/5 Gradient Descent Exercises Solution.ipynb')


def test_6_sol():
    _notebook_run('solutions/6 Convolutional Neural Networks Exercises Solution.ipynb')


def test_8_sol():
    _notebook_run('solutions/8 Recurrent Neural Networks Exercises Solutions.ipynb')


def test_9_sol():
    _notebook_run('solutions/9 Improving performance Exercises Solutions.ipynb')
