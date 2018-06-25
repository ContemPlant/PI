# Arduino Coordinator (RasPi)

## Usage

#### Prequesites

This project needs following dependencies

- Python version 3.6
- Python virtualenv
- Driver for serial ports

#### Installing
Enter virtualenvironment and install dependencies
```
virtualenv venv
source venv/bin/activate
pip install -r deps.txt
```

#### Usage
Start listening
```
python src/main.py
```

#### Testing
To run the test suite simply run
```
python -m unittest discover
```