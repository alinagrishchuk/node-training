# Misc
- Optimizing development flow
- Authentication & Authorization
- Logging
- Compression
- Deploying
- Security
- JSON template engine

---
# Optimizing development flow
- Yarn
- node-supervisor

---
# Yarn package manager
- [Yarn](https://yarnpkg.com/) is a new package manager for Node.js projects
- Mostly has the same API as for npm
- Faster and more reliable than npm
- Also supports lockfile (`yarn.lock`) to lock all the dependency versions (similar to `npm shrinkwrap`)
- Quite new and only just getting stable

---
# node-supervisor
- [node-supervisor](https://github.com/petruisfan/node-supervisor) looks for file changes and on change reloads the application automatically
- Supports debugging
- Usage:
```shell
npm install supervisor -g
supervisor index.js
```
- Another possibility: [nodemon](https://github.com/remy/nodemon)

---
# Authentication
- Process of validating the user is who she claims to be
- Usually done online by user providing username and password
- For APIs tokens are usually used because:
    - Single user can have multiple tokens
    - If one token is exposed, it can be easily disabled
    - Tokens can have explicit access restrictions and thus prevent possible damages on exposure

---
# Authentication in Express.js
- Implementing security-related things yourself is generally not smart
- Still, for the sake of example, authentication can be implemented as Express.js middleware:
```javascript
app.use((req, res, next) => {
    if (req.query.token === 'SECRET_TOKEN_TOKEN') {
        next();
    }
    else {
        res.status(401).send('Please sign in.');
    }
});
```

---
# Passport.js
- De facto standard authentication solution for Express.js applications
- Flexible & does not mount routes
- Supports OAuth (Facebook, Twitter, etc.) & OpenID ()
- Has over 300 login strategies available

---
# Passport.js - Username and password authentication (1)
Install:
```shell
npm install --save passport
```

Register the strategy:
```javascript
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
passport.use(new LocalStrategy(
    (username, password, done) => {
        if (username !== process.env.username || password !== process.env.password) {
            done(null, false, {message: 'Incorrect credentials.'});
            return;
        }
        return done(null, {});
    }
));
app.use(passport.initialize());
```

---
# Passport.js - Username and password authentication (2)
Login route:
```javascript
app.post('/login', 
  passport.authenticate('local', { failureRedirect: '/login' }),
  (req, res) => {
    res.redirect('/');
  });
```

---
# Token-based authentication
Ready strategy for token-basen authentication is available with `passport-localapikey` module:
```javascript
passport.use(new LocalAPIKeyStrategy(
  (apikey, done) => {
    if (apikey !== process.env.TOKEN) { return done(null, false); }
    return done(null, {});
  }
));
```

---
# Authentication errors
- If authentication credentials are bad, `done(null, false)` should be called
- If there happens an error, `done(error)` should be called

---
# Authorization
- After user is identified, it needs to be determined whether user has access to certain resource
- Often much more complicated than authentication

---
# acl
- Access Control List (ACL) module for authorization
- Role-based, hierarchical access control
- Supports Redis, MongoDB and in-memory backends with also 3rd-party backends for firebase, knex, etc.

---
# JWT

---
# Compression
To enable Gzip/deflate compression, `compression` can be used

```shell
npm install --save compression
```

```javascript
const compression = require('compression');
app.use(compression);
```

---
# Logging
- Request logging (access logs)
- Application logging

---
# Request logging (access logs)
- [Morgan](https://github.com/expressjs/morgan) allows easy logging of HTTP requests made to the server
- Supports multiple formats, including: [Apache combined](https://httpd.apache.org/docs/1.3/logs.html#combined) & [Apache common](https://httpd.apache.org/docs/1.3/logs.html#common)
- Available options: 
    - `immediate`: logs before response -> crash on handler doesn't prevent logging. Only request available.
    - `skip`: accepts function that tells whether logging should be skipped for certain request.
    - `stream`: stream to write in. Allows for example logging to stream.

---
# Morgan - Usage
Installation:
```shell
npm install --save morgan
```

Usage with Express.js:
```javascript
const morgan = require('morgan');
app.use(morgan('combined'));
```

`morgan('combined')` also accepts second parameter that is the options:
```javascript
const fs = require('fs');
const accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), {flags: 'a'});
morgan('combined', {
  skip: (req, res) => res.statusCode < 400,
  stream: accessLogStream
});
```

---
# Exercise
Add access logging for your application to file `access.log`. Log only if response status code is 2xx. 

---
# Application logging
- `console.log` limitations:
    - outputs only to single place: stdout
    - No possibility to set logging level (debug, info, warning, etc.)
    - No support for metadata
- Solution: [Winston](https://www.npmjs.com/package/winston) - simple and universal logging library

---
# Winston
- Decouples API to log and the transportation to storage
- Supports multiple simultaneous transportation targets
- Available loggers: console, file, http and memory. Custom ones allowed too.
- Objects can be passed as metadata
- Can also read back from the logs
- Filters and rewriters to filter and modify log entries before pushing forward

---
# Winston - Usage
Installation: 
```shell
npm install --save winston
```

Usage:
```javascript
const winston = require('winston');
 
winston.log('info', 'Hello distributed log files!');
winston.info('Hello again distributed logs');

winston.level = 'debug';
winston.log('debug', 'Now my debug messages are written to console!');
```

Default logger is console, to change for file use `winston.configure`:
```javascript
winston.configure({
    transports: [
        new (winston.transports.File)({ filename: 'somefile.log' })
    ]
});
```

---
# Exercise
Add application-level logging to your application with file target (application.log).

---
# Exercise
Add new end-point `/print-logs` that reads all the logs from the just implemented logger and shows them.

---
# Deploying
Most used solutions nowadays:
- AWS Elastic Beanstalk
- Docker
- Heroku

---
# AWS Elastic Beanstalk
- Just deploy your code and Beanstalk will take care of rest
- Creates and configures resources needed based on application type (e.g. AWS EC2 instances)
- Supports many languages and frameworks

---
# Beanstalk demo

---
# Docker
- Topic for its own training
- "Build once, run anywhere"
- Virtualized environment with everything necessary installed

---
# Heroku
- Really easy to get started
- Detects application type based on files, downloads dependencies and runs it
- Can deploy every time something is pushed to the GitHub
- Free tier available
- Easy to scale
- Usable URL for app: APP_NAME.herokuapp.com (e.g. URL of these slides)

---
# Heroku free tier
- Can only run certain amount of hours per month
- Go to sleep after 30min inactivity
- Start-up is somewhat slow 

---
# Procfile
- Format for specifying what Heroku should run
- Simple text file in the root of project
- Format:
```
web: node index.js
worker: node worker.js
```

---
# Security
- Helmet 
- CORS
- Dependency security
- Use TLS

---
# Helmet
- [Helmet](https://github.com/helmetjs/helmet) secures Express.js application by modifying multiple headers

---
background-position: center;
background-repeat: no-repeat;
background-size: contain;
background-image: url(misc/helmet-modules.png)

---
# Helmet - Usage
Installation: 
```shell
npm install helmet --save
```

Basic usage:
```javascript
const helmet = require('helmet');
app.use(helmet());
```

`helmet()` applies all default measures. To use only some, enable only those:
```javascript
app.use(helmet.noCache())
app.use(helmet.frameguard())
```
or disable some:
```javascript
app.use(helmet({
  frameguard: false
}));
```

---
# Exercise
Enable every default module of Helmet but the `X-Download-Options` header setting (`ieNoOpen`)

---
# CORS
- AJAX calls to other domains are forbidden by default by the [same-origin security policy](https://en.wikipedia.org/wiki/Same-origin_policy)
- Implemented by basically all browsers
- Can be relaxed by enabling `Access-Control-*` headers

---
background-position: center;
background-repeat: no-repeat;
background-size: contain;
background-image: url(misc/cors.png)
# 

---
# CORS with Express.js
- To enable Cross-Origin Resource Sharing (CORS), [cors package](https://github.com/expressjs/cors) can be used
- It supports enabling CORS for all routes, for single routes, and for pre-flight requests

---
# CORS - Usage
Installation:
```shell
npm install --save cors
```

Enable for all requests:
```javascript
const cors = require('cors');
app.use(cors());
```

---
# Exercise
Implement CORS so that your application only allows CORS for POST on path `/cors-enabled`.

---
# Dependency security
- "Security of your app is only as strong as the “weakest link” in your dependencies."
- To check your dependencies for known vulnerabilities, `nsp` can be used
```shell
npm i nsp -g
nsp check
```

---
# Exercise
Check your project for known vulnerabilities

---
# Use TLS
- TLS is the new progression of SSL
- Express.js can handle HTTPS [relatively simply](http://stackoverflow.com/a/5998795/1744702)
- Generally better to implement TLS in reverse-proxy such as Nginx

---
# JSON template engine
- Express.js can send JSON out-of-the-box (`res.json({})`)
- Sometimes there is a need for more granular control
- Example use cases:
    - Filtering our sensitive user data like passwords
    - Values need to be formatted before sending
    - Apply sub views
    - Caching views
    
---
# JSON template engine - Installation
```shell
npm install --save express-json-views
```

```javascript
const viewEngine = require('express-json-views');
app.engine('json', viewEngine({
       helpers: require('./views/helpers')
   }));
app.set('views', __dirname + '/views');
app.set('view engine', 'json');
```

---
# JSON Template engine - Views
```json
{
    "id": {},
    "slug": {
        "format": "getPostSlug"
    },
    "content": {
        "from": "content_text"
    },
    "comments": {
        "view": "comment"
    }
}
```
- Each key will be rendered to the response
- Values are interpreted as:
    - *{}*: Copies the value from the passed data.
    - *from*: Uses this value to lookup the value in the data object instead of the view key.
    - *format*: Calls a helper function with this name. Passes the value and the full object as arguments.
    - *view*: Defines the view if this value should be rendered with a different view. Value must be an Array or objects or an Object.