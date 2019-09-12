## Task

Design a CLI tool which should print firstname, lastname and given name itself from the given input.

### Conditions

1. While running the CLI tool 'name' should be mandatorily specified.
2. User can pass 'n' no. of arguments
3. Either of the optional arguments should be specified [firstname or lastname]

### Modules to be used

***Implementation should be done using argparse only***

### Implementation


#### Introduction

Argparse is python module to parse the command line arguments. Program defines the command line arguments and argparse figures out how to parse them through sys.argv. It also gifts us with help message on its own.

#### Steps to approach the task

*** How exactly does argparse parse the CLI arguments? ***

    import argparse
    parser = argparse.ArgumentParser()

First step, is creating ArgumentParser object. This object can thereby hold all the information which can be parsed in python data types. Every command line tool expects positional or optional arguments. Hence, we also expect our tool to behave in similar fashion.
Second step is adding arguments to the parser.
