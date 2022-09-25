[![CircleCI](https://circleci.com/gh/gradio-app/gradio.svg?style=svg)](https://circleci.com/gh/gradio-app/gradio)  [![PyPI version](https://badge.fury.io/py/gradio.svg)](https://badge.fury.io/py/gradio)  [![codecov](https://codecov.io/gh/gradio-app/gradio/branch/master/graph/badge.svg?token=NNVPX9KEGS)](https://codecov.io/gh/gradio-app/gradio) [![PyPI - Downloads](https://img.shields.io/pypi/dm/gradio)](https://pypi.org/project/gradio/) [![Twitter Follow](https://img.shields.io/twitter/follow/gradio.svg?style=social&label=Follow)](https://twitter.com/gradio)

#  Welcome to Gradio

Quickly create beautiful user interfaces around your machine learning models. Gradio (pronounced GRAY-dee-oh) makes it easy for you to demo your model in your browser or let people "try it out" by dragging-and-dropping in their own images, pasting text, recording their own voice, etc. and seeing what the model outputs.  

![Interface montage](website/homepage/src/assets/img/montage.gif)

Gradio is useful for:

* **Demoing** your machine learning models for clients / collaborators / users / students

* **Deploying** your models quickly with automatic shareable links and getting feedback on model performance

* **Debugging** your model interactively during development using built-in manipulation and interpretation tools

**You can find an interactive version of the following Getting Started at [https://gradio.app/getting_started](https://gradio.app/getting_started).**

{% with code=code, demos=demos %}
{% include "guides/getting_started.md" %}
{% endwith %}

##  System Requirements:

Gradio requires Python `3.7+` and has been tested on the latest versions of Windows, MacOS, and various common Linux distributions (e.g. Ubuntu). For Python package requirements, please see the `setup.py` file.

##  Contributing:

If you would like to contribute and your contribution is small, you can directly open a pull request (PR). If you would like to contribute a larger feature, we recommend first creating an issue with a proposed design for discussion. Please see our [contributing guidelines](https://github.com/gradio-app/gradio/blob/master/CONTRIBUTING.md) for more info.

##  License:

Gradio is licensed under the Apache License 2.0


##  See more:

You can find many more examples as well as more info on usage on our website: www.gradio.app

See, also, the accompanying paper: ["Gradio: Hassle-Free Sharing and Testing of ML Models in the Wild"](https://arxiv.org/pdf/1906.02569.pdf), *ICML HILL 2019*, and please use the citation below.

```
@article{abid2019gradio,
title={Gradio: Hassle-Free Sharing and Testing of ML Models in the Wild},
author={Abid, Abubakar and Abdalla, Ali and Abid, Ali and Khan, Dawood and Alfozan, Abdulrahman and Zou, James},
journal={arXiv preprint arXiv:1906.02569},
year={2019}
}
```
