# Templatify

## Setup
1. Clone this repository to your local directory.
2. Create a virtualenv environment and activate it.
```
python3 -m venv venv
source venv/bin/activate
```
3. Install the command to your environment.
```
python -m pip install --editable .
```

## Usage
Make sure your virtualenv is still activated.
```
source venv/bin/activate
```

* To convert internal asset links:
```
templatify assets <your-filename.html>
```

* To convert internal hyperlinks:
```
templatify links <your-filename.html>
```