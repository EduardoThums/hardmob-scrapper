# HardMOB Scrapper
Script to scrap [HardMOB](https://www.hardmob.com.br/forums/407-Promocoes) promotions site given a specify keyword

## Installation

### Environment
Create a python virtual environment and install the required dependencies through ```requirements.txt``` file using pip:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configure drivers
Selinium uses interface drivers to work with browsers, so you need to download a driver of your preference and put it into ```drivers``` folder.
For more information about how Selenium work with drivers see [Selenium Drivers](https://selenium-python.readthedocs.io/installation.html#drivers)

## Usage
Example of search given "phones" as keyword:
```
python app.py -w phones
```


## Update

This scrap method doesn't work anymore :(

They added captchas to block the search through the pages.

This repo will remaing archived until they remove the captcha or someone find a better solution.
