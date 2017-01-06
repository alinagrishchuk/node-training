# Node.js

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
```
node my-script.js
```

---
# Exercise
Create file `script.js` that simply calls `console.log('It is alive')`, and run it.

---
# Accessing the environment variables
- Available as `process.env.VARIABLE`:
```
console.log(process.env.VARIABLE);
```

On Windows you can set the environment variables for script as:
```
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
```
npm install -g angular-cli
ng new MY_PROJECT
```

Local:
```
npm install underscore
```

```
const _ = require('underscore')
```

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
```
npm init
```

and answer all the interactive questions to populate simple package.json

---
# Installing dependencies
Install all dependencies (`dependencies` & `devDependencies`):
```
npm install
```

Install only `dependencies`:
```
npm install --production
```
Same happens if `NODE_ENV` environment variable is set to _production_.

All dependencies are stored to `node_modules` folder.

---
# Adding new dependencies
To add a new dependency for your project, you can use 
```
npm install --save express@4.14.0
```
which installs the new package to `node_modules` and adds it to the `package.json`.

`--saveDev` to store as `devDepencency`.

Using the dependencies: `const express = require('express')`

---
# Custom npm scripts
`package.json` can contain field called `scripts` that contains an object with custom scripts to be executed with `npm run SCRIPT_NAME`.
 
```
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
```
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
