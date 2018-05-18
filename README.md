# PySmoke

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
post_id: 1
user_id: 1
```

__Test file example:__

```markdown
[login]
url: /auth/login
method: POST
authorization: None
payload: {"username": "test@test.com", "password": "test1234"}
tests:
	http_status: 200
	headers.Location: true
	result: true
	result.version: true
```

__Commands:__

| Command | Options | Description |
|---------|---------|-------------|
| `$ python pysmoke.py` | --help | Display help menu |
| `$ python pysmoke.py`| | Run all the tests in all the groups |
| `$ python pysmoke.py` | --verbose | Run all the tests on verbose mode |
| `$ python pysmoke.py` | --filter get.test | Run all the tests on the get.test group |
| `$ python pysmoke.py` | --filter get.test:list | Run the list test on the get.test group |

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
