# PySmoke

PySmoke is a command line tool to run smoke tests in your REST API using python and just config files.

The idea was born during a manual test with the testers of my current project, we where looking for a solution to automate smoke tests that requires little to no programming skills to work with and let the testers team check basic stuff on the API side with a basic fixture.

This is a work in progress and I'm working on it during my spare time.

## Example

```markdonw
[login]
url: /auth/login
method: POST
authorization: None
payload: {"username": "test@test.com", "password": "test1234"}
tests:
	http_status: 200
	result: true
	result.version: true
```

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
