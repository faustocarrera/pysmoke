# PySmoke

Smoke tests for your REST API using python and just config files

The idea was born during a manual test with the testers of my current project, we where looking for a solution to automate smoke tests that requires little to no programming skills to work with and let the testers team check basic stuff on the API side with a basic fixture. 

This is a work in progress and I'm working on it during my spare time.

## Example

```markdonw
[login]
url: /auth/login
method: POST
authorization: None
payload: {"username": "test@test.com", "password": "test1234"}
tests: {"token": true, "id": true}
```

```
python run.py
```