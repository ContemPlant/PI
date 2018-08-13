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

Start listening
```
python src/main.py
```
To run the script in failsafe mode 
```
./start.sh
```


#### Testing
To run the test suite simply run
```
python -m unittest discover
```

## Built With

- [python-xbee](https://github.com/digidotcom/python-xbee)


## License
This project is licensed under the MIT License


## Acknowledgements

- Used code from [Python GraphQL Client](https://github.com/prismagraphql/python-graphql-client)
