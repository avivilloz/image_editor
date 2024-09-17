# PKG

short_pkg_description

## Description:

long_pkg_description

## How to install:

Run the following command in your python venv:

```bash
pip install git+https://github.com/avivilloz/pkg_name.git@main#egg=pkg_name
```

Or add the following line to your project's `requirement.txt` file:

```
git+https://github.com/avivilloz/pkg_name.git@main#egg=pkg_name
```

And run the following command:

```bash
pip install -r requirements.txt
```

## How to use:

`file.py`
```python
from pkg_name import pkg_function

# Use pkg_function
```