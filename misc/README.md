# Misc
- Optimizing development flow
- Logging
- Deploying
- Security

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
```
npm install supervisor -g
supervisor index.js
```
- Another possibility: [nodemon](https://github.com/remy/nodemon)

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
```
npm install --save morgan
```

Usage with Express.js:
```
const morgan = require('morgan');
app.use(morgan('combined'));
```

`morgan('combined')` also accepts second parameter that is the options:
```
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
```
npm install --save winston
```

Usage:
```
const winston = require('winston');
 
winston.log('info', 'Hello distributed log files!');
winston.info('Hello again distributed logs');

winston.level = 'debug';
winston.log('debug', 'Now my debug messages are written to console!');
```

Default logger is console, to change for file use `winston.configure`:
```
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


---
# Security
- Helmet 
- CORS

---
# Helmet
- [Helmet](https://github.com/helmetjs/helmet) secures Express.js application by modifying multiple headers
![Helmet modules](misc/helmet-modules.png "Helmet modules")

---
# Helmet - Usage
Installation: 
```
npm install helmet --save
```

Basic usage:
```
const helmet = require('helmet');
app.use(helmet());
```

`helmet()` applies all default measures. To use only some, enable only those:
```
app.use(helmet.noCache())
app.use(helmet.frameguard())
```
or disable some:
```
app.use(helmet({
  frameguard: false
}));
```

---
# Exercise
Enable every default module of Helmet but the `X-Download-Options` header setting (`ieNoOpen`)

---
# CORS

---
# CORS with Express.js
- To enable Cross-Origin Resource Sharing (CORS), [cors package](https://github.com/expressjs/cors) can be used
- It supports enabling CORS for all routes, for single routes, and for pre-flight requests

---
# CORS - Usage
Installation:
```
npm install --save cors
```

Enable for all requests:
```
const cors = require('cors');
app.use(cors());
```

---
# Exercise
Implement CORS so that your application only allows CORS for POST on path `/cors-enabled`.