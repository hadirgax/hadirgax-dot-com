---
title: "Anaconda Configuration"
author: "Hadir Garcia-Castro"
date: 2017-12-20T11:53:49-07:00
description: "Anaconda distribution configuration."
type: technical_note
layout: Anaconda
draft: false
---

# Create a virtual environment
To create new python a virtual environment in an specific folder and with an specific python version:

.. code-block:: bash
    conda create -p ~/pyenvs/djenv35 python=3.5 or python to install the same version installed with conda

To create the environment into the default anaconda's :bash:'env' folder

.. code-block:: bash
    conda create -n djenv35 python=3.5

to activate/deactivate it when create into a specific path folder, type on terminal:

.. code-block:: bash
    source activate ~/pyenvs/djenv35
    source deactivate ~/pyenvs/djenv35

to activate/deactivate it when create into anaconda's default env folder, type on terminal:

.. code-block:: bash
    source activate djenv35
    source deactivate [djenv35]

to remove an environment created in specific folder path:

.. code-block:: bash
    conda remove -p /home/user/env_name --all

To remove it when created into the anaconda's env folder:

.. code-block:: bash
    conda remove --name env_name --all


To view the anaconda's environments

.. code-block:: bash
    conda info --envs
