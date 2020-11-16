# gotrack
Track the duration of your travel time between home and work and export it to a csv file. 

## Installation
1. Install depencies from `requirements.txt` with `pip install -r requirements.txt`.
2. Create an API key on
[developer.here.com](https://developer.here.com/develop/rest-apis).

## Usage
Provide the apikey, homelocation, worklocation and outputfile via cli parameters (see `./main.py --help` for usage). It's possible to provide the API key by setting the environment var `GOTRACK_APIKEY`.

Example: `./main.py -h "<HOME ADDRESS>" -w "<WORK ADDRESS>" -o "<OUTPUTFILE>" -a "<APIKEY>"`

## License
MIT License
