# Projet 1

The questions are inside of the [projet.pdf](./assets/projet.pdf) file.

Source code is under the [src](./src/) folder

## Usage

First, thie next two steps are completely optional but it's a good practice to create vertual environment for your project to avoid polluting your global python environment.

```sh
python -m venv .venv
```

Then activate the newly created virtual environment.

```sh
source .venv/bin/activate
```

Now for the **mandatory** step, you need to install all dependencies.

```sh
pip install -r requirements.txt
```

The solution can be run via:

```sh
streamlit run ./src/calcul_web.py
```
