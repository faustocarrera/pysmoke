## Analysis: Pysmoke CLI Test Framework

### Overview
Pysmoke is a command-line tool designed to run smoke tests against API endpoints. It parses JSON test configuration files containing HTTP request details and expected outputs, constructs and executes these API calls utilizing `requests`, and dynamically validates the resulting HTTP responses based on nested property paths and expected status codes.

### Entry Points
- `pysmoke.py:17` - `cli()` function decorated with `click.command()` serving as the program's main execution entry point.
- `smoke/smoketests.py:51` - `run()` method in the `SmokeTests` class that triggers test loading and test thread execution.

### Core Implementation

#### 1. CLI and Initialization (`pysmoke.py:17-22` & `smoke/smoketests.py:20-37`)
- Captures command-line arguments (config_path, source_path, filter, verbose) using `click`.
- Instantiates the `SmokeTests` framework, initializing all configuration singletons, utility services, request wrappers (`ApiCalls`), and response validators (`Validator`).

#### 2. Test Configuration Management (`smoke/testconfig.py:17-27` & `smoke/smoketests.py:57-87`)
- Loads JSON test files via `TestConfig.load()` utilizing Python's `json` parser at `smoke/testconfig.py:23`.
- Collects test steps into a flat `tests_to_run` dictionary using a `compose()` loop, generating distinct hash keys via `uuid1` at `smoke/smoketests.py:84`.
- Filters tests if a target test class or subset target (`self.single_test`) is set using command-line arguments at `smoke/smoketests.py:44`.

#### 3. API Invoker Logic (`smoke/apicalls.py:22-44`)
- Reads request elements (`url`, `authorization`, `payload`) from parsed configurations and replaces environment variables dynamically using `self.utils.vars_replace` at `smoke/apicalls.py:24-27`.
- Executes synchronous GET, POST, PUT, or DELETE request based on the matched method at `smoke/apicalls.py:32`.
- Transforms raw payload checking types at `smoke/apicalls.py:70`.

#### 4. Test Assertion Pipeline (`smoke/validator.py:15-37`)
- Triggers assertions on the API payload response mapping against configured expected parameters parsed from tests.
- Uses `__get_value` at `smoke/validator.py:66` utilizing dot notation indexing to map and traverse the response payload dict layers (i.e., `headers.content-type`).
- Evaluates individual test assertions strictly comparing the generated request with the structured JSON properties at `smoke/validator.py:117-134`.

### Data Flow
1. CLI invokes test execution loop over `config_path` inside `pysmoke.py:22`.
2. `SmokeTests` resolves test suites natively calling `run_tests(key)` in `smoke/smoketests.py:95`.
3. Test elements are aggregated formatting variables into a request wrapper via `ApiCalls.call(test)` locally calling request modules.
4. `requests` module completes API network calls returning parsed response outputs alongside elapsed payload execution into `smoke/apicalls.py:42`. 
5. The extracted result network format passes directly into `Validator.test()` alongside parsed list assertion structures within `smoke/smoketests.py:117`.
6. `Validator` traverses JSON layers dynamically validating and logging outputs onto `self.errors` via index tracking inside `smoke/validator.py:61-64`.

### Key Patterns
- **Facade Pattern:** `SmokeTests` acts as a facade orchestrating specialized modules (`AppConfig`, `Validator`, `ApiCalls`) seamlessly routing the execution flow.
- **Wrapper Logic:** `ApiCalls` sits behind the testing engine obscuring execution parameters and underlying system handling of the `requests` library outputs cleanly mapped over standardized formats inside `smoke/apicalls.py:78`.

### Configuration
- Application parameters configured mapped parsing configuration subsets explicitly via `AppConfig` locally at `smoke/appconfig.py:10`, interpreting endpoints and tracking SSL properties locally inside custom loaders (`app.url`, `app.ssl_verify`).
- Variables read via mapped `AppConfig.vars()` loop resolving targets mapping tests inside logic via iterations loop (`smoke/appconfig.py:28`). 
- Target test definition trees sourced natively iterating through nested arrays in `tests/` structured configurations dynamically via `load_tests()`.

### Error Handling
- Request configuration handlers force standard exceptions safely raising `'Error, method not recognized'` when hitting an invalid HTTP caller (`smoke/apicalls.py:43`).
- Assertion property tracking skips internal errors catching properties naturally logging list discrepancies onto a structural tracking variable `self.errors` via `Validator.__add_error()` tracked silently checking failures (`smoke/validator.py:61-64`).
- CLI loops summarize logs displaying the aggregate failure counts at runtime returning an explicitly caught CLI termination returning `sys.exit(1)` internally on explicit test failures or 0 silently completing standard routines (`smoke/smoketests.py:147-161`).
