Python - Test-driven development
---

![](https://media.giphy.com/media/3orieQ0mh5Mi5vSZZC/giphy.gif)

## Doctest

> The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown

There are several common ways to use doctest:

- To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
- To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
- To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.


## Unit test

```python
import unittest

# class of your test
```

### test fixture

> A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

### test case

> A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

```python
import unittest

class TestStringMethods(unittest.TestCase):
    # code your tests case there
```

### test suite

> A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

```python
# import your test modules
import scenario
import thing

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add tests to the test suite
suite.addTests(loader.loadTestsFromModule(scenario))
suite.addTests(loader.loadTestsFromModule(thing))
```

### test runner

> A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

```python

# See the code previously

# Initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

```


References
---

* [doctest](https://docs.python.org/3.4/library/doctest.html)

* [unittest](https://docs.python.org/3.4/library/unittest.html)
