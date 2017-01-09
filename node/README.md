# Node.js
- What is it?
- Using Node.js
- npm
- Splitting code in multiple files
- Package.json
- Testing

---

# What is Node.js?
- "Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine." 
- "Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient."
- "Node.js' package ecosystem, npm, is the largest ecosystem of open source libraries in the world."

---
# History
- Initial release May 27, 2009 by Ryan Dahl
- Latest stable versions 7.3.0 & 6.9.2 (December 2016)
- Version jump from 0.12.x to 4.x

---
# Versioning
- Details can be found from [nodejs/LTS repository](https://github.com/nodejs/LTS) in GitHub
- Even-numbered versions (4, 6, 8, ...)
    - LTS (Long-Term Support) versions
    - Released every April (v8 in April 2017)
    - Supported for 6 (current) + 18 (LTS) + 12 (maintenance) = 36 months (3 years) 
- Odd-numbered versions (5, 7, 9, ...)
    - For newest features
    - Released every October
    - No LTS or maintenance

---
# Versioning history
![Node.js versioning](node/versioning.png "Node.js versioning")

---
# Version schedule
![Node.js schedule](node/schedule.png "Node.js schedule")

---
# ES6 support
- Node 6.x has over 92% of ES6 features implemented
- Node 7.x already on 99%

---
# Usage
Run the script with
```shell
node my-script.js
```

---
# Exercise
Create file `script.js` that simply calls `console.log('It is alive')`, and run it.

---
# Accessing the environment variables
Available as `process.env.VARIABLE`:
```javascript
console.log(process.env.VARIABLE);
```

You can set the environment variables for script as:
```shell
VARIABLE=ABC node my-script.js
```

---
# Exercise
Modify the previously created `script.js` to print `SECRET_TOKEN` given as environment variable and run it.

---
# Debugging

---
# npm
- npm (Node Package Manager) is the package manager for Node.js
- Has the most modules of any package manager for any language
- Comes along with Node.js when installed
- Available on command line with `npm` command
- Can update itself with
```
npm install -g npm
```

---
# Global vs. local packages
Global packages:
- Installed globally with `-g` switch for `npm install`
- Provide some command-line commands

Local packages
- Installed to the `node_modules` folder under current folder
- Available only for the current project with `require`

---
# Global vs. local packages - usage
Global:
```shell
npm install -g angular-cli
ng new MY_PROJECT
```
(You might need `sudo` for `npm install -g` on Linux and OS X)

Local:
```shell
npm install underscore
```

```javascript
const _ = require('underscore')
```

---
# Exercise
## Global package
Install Express generator globally (package name: `express-generator`), and use it to generate a project (command: `express myapp`).

## Local package
Install underscore locally and use it to modify your logging string somehow. Use underscore's [max](http://underscorejs.org/#max) function to select max age from array `[{age: 24}, {age: 45}, {age: 4}, {age: 20}]`.

---
# Splitting code between multiple files
- `module.exports` is used to declare what is exported from the file

_file1.js_
```javascript
function getText() {
    return 'My text';
}

module.exports = getText;
```

- `require()` with local path (`.` for current folder) is used to get that value

_file2.js_
```javascript
const getText = require('./file1'):
console.log(getText());
```

---
# Splitting code between files
- Often the exports are objects to allow multiple things to be exported:

_get-methods.js_
```javascript
module.exports = {
    getA: () => 'A', 
    getB: () => 'B'
};
```

_index.js_
```javascript
const getMethods = require('./get-methods');
console.log(getMethods.getA());
```

---
# Splitting code between files
- Defining all exports with `module.exports` at the bottom of file is somewhat clear solution
- What Node.js does internally, is that it includes the following line at the start of each file:
```javascript
var exports = module.exports = {};
```
because of this we can also write our code this way:
```javascript
exports.getA = () => 'A'; 
exports.getB = () => 'B';
```

---
# Exercise
Declare another file where you export a function to give the value to be logged and use it in the `script.js`.

---
# Package.json
- JSON file to define an npm project
- Can contain:
    - Project name, description, version, license etc.
    - Dependencies
    - Required node version (`engines`)
    - npm scripts (covered later)
    - etc.

---
# Dependencies
- Multiple types of dependencies:
    - `dependencies` for actual run-time dependencies
    - `devDependencies` for development-time dependencies such as test frameworks and bundlers
    - `peerDependencies` for requiring certain versions of other modules to be installed when used (used for example for plugins)
    - `optionalDependencies` for platform-specific (Windows, OS X, etc.) packages for optimization purposes
- Dependencies can point to npm registry, Git repository, tar ball, local path
- Dependency versions can be specified as specific, greater/lower than, ranges, etc.
    
---
# Initializing new project
Run
```shell
npm init
```

and answer all the interactive questions to populate simple package.json

---
# Installing dependencies
Install all dependencies (`dependencies` & `devDependencies`):
```shell
npm install
```

Install only `dependencies`:
```shell
npm install --production
```
Same happens if `NODE_ENV` environment variable is set to _production_.

All dependencies are stored to `node_modules` folder.

---
# Adding new dependencies
To add a new dependency for your project, you can use 
```shell
npm install --save express@4.14.0
```
which installs the new package to `node_modules` and adds it to the `package.json`.

`--saveDev` to store as `devDepencency`.

Using the dependencies: `const express = require('express')`

---
# Custom npm scripts
`package.json` can contain field called `scripts` that contains an object with custom scripts to be executed with `npm run SCRIPT_NAME`.
 
```shell
{
    "scripts": {
        "test": "karma run",
        "create-some-folder": "mkdir some && cd some && mkdir other"
    }
}
```

---
# Pre and post
- All scrips can have pre and post steps
```json
{
    "scripts": {
        "pretest": "do-something-before-test",
        "test": "karma run",
        "posttest": "do-something-after-test"
    }
}
```
- Also available for other commands like `install`

---
# Exercises
1. Create a folder `ex-node` and initialize it as npm module
2. Create a script that prints "ex-node started" and run the script with `node` command
3. Add a `start` script to `package.json` and use it to run the script as `npm start`
4. Add [`strman`](https://github.com/dleitee/strman) as a dependency (should also be in `package.json`) and use it for logging.

---
# Testing
- Two main libraries are Jasmine and Mocha - both equally used
- Mocha provides a little more flexibility (e.g. no assertion or mocking included)
- Jasmine is batteries-included solution
- Same high-level API for both
- On this training Jasmine is used

---
# Jasmine
- Behavior Driven Development testing framework
- For both browser and Node.js projects
- Runners also available for Ruby-based (Rails, Sinatra, etc.) and Python-based (Django, Flask, etc.) web frameworks

---
# Jasmine - Usage
Installation:
```shell
npm install --save-dev jasmine
jasmine init
```
Initializing will create `jasmine.json` for configuration such as test file look-up path

Run jasmine tests:
```shell
jasmine
``` 

---
# Exercise
Run the above commands to find out there aren't any test cases yet

---
# Jasmine test case
Example spec:
```javascript
describe("A suite is just a function", () => {
  it("and so is a spec", () => {
    const a = true;
    expect(a).toBe(true);
  });
});
```

---
# Setup and tear-down
- `beforeEach`, `afterEach`, `beforeAll`, and `afterAll`
- Example:
```javascript
describe('', () => {
    beforeEach(() => {
        console.log('This is printed before each it block');
    });
});
```

---
# Exercise
- Write a function `getData` (in test file or as separate file) that returns data as `{persons: [{name: 'obj1'}, {name: 'obj2'}]}`.
- To test your function, check that it returns an object with list `persons` of length 2.

---
# Asynchronous tests
Consider we have a function that is asynchronous (timeouts, AJAX requests, etc.):
```javascript
const myFn = (cb) => {
    setTimeout(() => {
        cb(200, {items: []});
    }, 1000);
};
```

to test this, we need to register appropriate callback and when it is called check the parameters
```javascript
describe("..", () => {
    it("..", (done) => {
        myFn((status, data) => {
            expect(status).toBe(200);
            expect(data.items.length).toBe(0);
            done();
        });
    });
});
```

---
# Exercise
Since the data of last exercise actually needs to be retrieved from the server, adjust the function to take a callback, that is invoked after 1 second with data as parameter.
Once modified, make your test compliant with this asynchronous behaviour.

---
# Matchers
- Matchers are used to determine whether the value produced by code under test is correct
- Jasmine provides a lot of [ready-made matchers](https://jasmine.github.io/2.5/introduction#section-Included_Matchers), such as:
    - `toEqual`, `toBe`
    - `toBeDefined`, `toBeNull`
    - `toContain`
    - `toThrow`
- You can also make your own matchers

---
# Custom matcher
- Repetitive matching can be implemented as custom matcher
- Matchers need to be registered in `beforeEach` block with `jasmine.addMatchers`
- `addMatchers` takes an object containing matcher factories:
```javascript
jasmine.addMatchers({
    toBeOneBiggerThan: () => {
        return {
            compare: (actual, expected) => {
                const pass = actual === expected + 1;
                const message = pass ? '' : `Expected ${actual} to be ${expected + 1}`; 
                return {
                    pass,
                    message
                }
            }
        }
    }
});
expect(3).toBeOneBiggerThan(2);
```

---
# Exercise
Make a custom matcher that checks that array passed to it contains the two objects you used in earlier exercise.
Use this new matcher instead of current check for two items.

---
# Spies
- Mocking is implemented in Jasmine as spies
- Makes it possible to track calls to functions
- Can also be used to change return values of functions
- Own set of matchers like `toHaveBeenCalled`, `toHaveBeenCalledTimes` and `toHaveBeenCalledWith`

---
# Spies - Example
```javascript
describe("A spy, when configured to call through", () => {
    let foo, bar, fetchedBar;
    beforeEach(() => {
        foo = {
            setBar: value => bar = value,
            getBar: () => bar
        };
        spyOn(foo, 'getBar').and.callThrough();
        foo.setBar(123);
        fetchedBar = foo.getBar();
    });

    it("tracks that the spy was called", () => {
        expect(foo.getBar).toHaveBeenCalled();
    });
    it("should not affect other functions", () => {
        expect(bar).toEqual(123);
    });
    it("when called returns the requested value", () => {
        expect(fetchedBar).toEqual(123);
    });
});
```

---
# Exercise
Declare on object called `fetcher` with two functions:
- `fetch`: return the value returned by `this.fetchInternal(n)` where `n` is number given as parameter
- `fetchInternal`: returns array of `n` items each one bigger than previous one
 
Test that when fetch is called:
- `fetch` returns list of correct length 
- `fetchInternal` is called with parameter that is given 
- `fetchInternal` is called exactly once