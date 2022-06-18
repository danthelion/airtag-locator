# Great Expectations

[Great Expectations](https://docs.greatexpectations.io/docs/) helps data teams eliminate pipeline debt, through data testing, documentation, and profiling. From the documentation:

> Great Expectations is the leading tool for validating, documenting, and profiling your data to maintain quality and improve communication between teams. Head over to our [getting started](https://docs.greatexpectations.io/docs/tutorials/getting_started/intro) tutorial.

## Adding and Installing

Install with Meltano:

```shell
meltano add utility great_expectations
# now try it out!
meltano invoke great_expectations --help
```

If you are using Great Expectations to validate data in a database or warehouse, you
might need to install the appropriate drivers. Common options are supported by Great Expectations
as pip extras, and any additional packages you may want can be added too by configuring
a custom `pip_url` for the `great_expectations` utility:

```shell
# set the _pip_url extra setting
meltano config great_expectations set _pip_url "great_expectations[redshift]; awscli"
# re-install the great_expectations plugin for changes to take effect
meltano install utility great_expectations
```

## Getting Started

Initialise your Great Expectations project:

```shell
# from your Meltano project root
cd utilities
meltano invoke great_expectations init
```

Congratulations, you just created your project! You can customise your configuration in many ways. Here are some examples:

```shell
# connect to your data
meltano invoke great_expectations datasource new
# bundle data with Expectation Suite(s) in a Checkpoint for later re-validation
meltano invoke great_expectations checkpoint new <checkpoint_name>
# create, edit, list, profile Expectation Suites
meltano invoke great_expectations suite --help
# build and manage Data Docs sites
meltano invoke great_expectations docs --help
```

If you chose to initialise Great Expectations in a folder other than `$MELTANO_PROJECT_ROOT/utilities/great_expectations`, configure your chosen directory in Meltano:

```shell
# view available great_expectations settings
meltano config great_expectations list
# set the `ge_home` to your chosen path
meltano config great_expectations set ge_home '$MELTANO_PROJECT_ROOT/<custom path>/great_expectations'
```