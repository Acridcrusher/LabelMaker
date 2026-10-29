# Setup
### requirements
- Python 3.12 or above
	- pip
- flask
- wkhtmltopdf

### Prep
Install Python 3.12 or above (3.13 in this example) using either the online installer or winget as this is needed as the web host using flask. Wkhtmltopdf to convert the html files to pdf for printing. 

The below section will walk through how to install the required modules

#### Python
##### online installer
Download Python using the following link [python 3.13](https://www.python.org/downloads/latest/python3.13/)

run the installer and continue through the setup and approve the admin installation request

##### winget
run the below winget commands to install python

```powershell
winget install --id "python.python.3.13"
```
or
```powershell
winget install --id 9PNRBTZXMB4Z
```

#### Pip
make sure pip is installed or install it through the bellow command
confirm if pip is installed
```Python
pip -V
```

if its not installed use the below command to install it.
```Python
python -m pip install --upgrade pip
```
#### flask
run the below pip command to install flask
```cmd
pip install flask
```

#### wkhtmltopdf
install the html to pdf converter
```cmd
pip install wkhtmltopdf
```
