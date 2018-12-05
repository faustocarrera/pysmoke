PySmoke
=======

PySmoke is a command line tool to run smoke tests in your REST API using python and just config files.

The idea was born during a manual test with the testers of my current project, we where looking for a solution to automate smoke tests that requires little to no programming skills to work with and let the testers team check basic stuff on the API side with a basic fixture.

This is a work in progress and I'm working on it during my spare time.

## Using the library

You have a single config file app.conf located on the `config/` folder holds the API URL and other variables used on your tests, and several test files called test groups, located on the `tests/` folder. All the tests files have the .test extension.

__Config example:__

```markdown
[app]
url: https://jsonplaceholder.typicode.com

[vars]
user_name: test@test.com
password: test1234
```

__Test file example:__

```markdown
[login]
url: /auth/login
method: POST
authorization: None
payload: {"username": "%username%", "password": "%password%"}
tests:
	http_status: 200
	headers.Location: True
	result: True
	result.version: True
	result.license: GNU
```

In this case we are testing the JSON response

```
{
  "result": {
    "version": "1.0",
    "last_update": "2018-12-05",
    "license": "GNU"
  }
}
```

The test should check the http status must be 200, the headers must contain the Location attribute, there must be a result attribute, inside the result attribute, a version attribute must exists, a license attribute must exists and must be equal to GNU.

__Validation rules:__

| Rule         | Description                                                           | Status      |
|--------------|-----------------------------------------------------------------------|-------------|
| True         | The attribute must exist on the JSON response                         | Implemented |
| False        | The attribute must not be present                                     | Implemented |
| Value        | The attribute value must exist and be equal to Value                  | Implemented |
| isnumber     | The attribute value must exist and must be a number                   | Future      |
| isstring     | The attribute value must exist and must be a string                   | Future      |
| islist       | The attribute value must exist and must be a list                     | Future      |
| isdictionary | The attribute value must exist and must be a dictionary               | Future      |
| ismail       | The attribute value must exist and must be a valid e-mail             | Future      |
| isdate       | The attribute value must exist and must be a valid date               | Future      |
| isdatetime   | The attribute value must exist and must be a valid datetime           | Future      |
| isdateiso    | The attribute value must exist and must be a valid date in ISO format | Future      |

__Commands:__

| Command               | Options                | Description                             |
|-----------------------|------------------------|-----------------------------------------|
| `$ python pysmoke.py` | --help                 | Display help menu                       |
| `$ python pysmoke.py` |                        | Run all the tests in all the groups     |
| `$ python pysmoke.py` | --filter get.test      | Run all the tests on the get.test group |
| `$ python pysmoke.py` | --filter get.test:list | Run the list test on the get.test group |
| `$ python pysmoke.py` | --verbose              | Run all the tests on verbose mode       |
| `$ python pysmoke.py` | --config ./app.conf    | App configuracion file                  |
| `$ python pysmoke.py` | --source ./tests       | Tests folder                            |

## How to start with the project

Clone the project:

```
$ git clone git@github.com:faustocarrera/pysmoke.git
```

Or download it:

```
$ wget https://github.com/faustocarrera/pysmoke/archive/master.zip
```

You could use virtualenv or install everything globally.

```
$ virtualenv env -p python3
$ env/bin/pip install -r requirements
```

Setup your API url on the `config/app.conf` file.  
Modify or create test inside the tests folder, all the tests must have the .test extension.  
Run the app.

```
$ env/bin/python pysmoke.py
```

Run it on verbose mode.  

```
$ env/bin/python pysmoke.py -v
```
