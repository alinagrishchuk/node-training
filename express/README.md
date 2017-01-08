# Express.js

---
# What is Express.js?
- De facto standard for web servers on Node.js
- High performance without complicated configuration
- Easy-to-use and minimal
- Supports multiple template engines (pug, handlebars, etc.)

---
# History
- Initial release in January 2010
- Current stable major 4.0.0 out in April 2014
- 4.14.0 latest as of 16.6.2016
- V5 in alpha.2

---
# Installation
```shell
npm install express --save
```

_index.js_
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000);
```

```shell
node index.js
```

---
# Exercise
Start your own project
```shell
mkdir ex-express
cd ex-express
npm init
npm install --save express
# Create index.js with the code from previous slide
node index.js
```

and now check `localhost:3000` on your browser.

---
# Responding to requests
- Routes are declared as
```javascript
app.METHOD(PATH, HANDLER)
```
for example
```javascript
app.get('/', (req, res) => {
    res.send('Hello World!');
});
```

---
# Paths
Paths can be:
- Strings
```javascript
app.get('/path', ..);
```
- Path pattern (based on [path-to-regexp](https://www.npmjs.com/package/path-to-regexp))
```javascript
app.get('/path/:id', ..);
```
- Regexps (Regular expressions)
```javascript
app.get(/\path1/|\/path2/g, ..);
```
- Array
```javascript
app.get(['/path1', '/path2'], ..);
```

---
# Handlers
- Handler functions have two parameters
    - `req`: Information, such as parameters, data and cookies, about the request 
    - `res`: Response object to construct and send the response back
- Example
```javascript
app.get('/', (req, res) => {
    const ip = req.ip;
    res.send(`Hello ${ip}`);
});
```
- If no response is sent, the request will hang (browser waits until timeout)

---
# Request
- The [Request](http://expressjs.com/en/4x/api.html#req) contains all of the information about the request:
- Most usual information needed:
    - Query parameters: `localhost/?asd=foo` `req.query.asd`
    - Request params (`/path1/:param1`): `req.params.param1`
    - Cookies: `req.cookies['my-cookie']`
    - Request info: `req.ip`, `req.hostname`, etc.
    - Request body (data): Covered later

---
# Exercise
- On GET `/` logs the request IP and query parameter called `myParam`
- On GET `/path1/:param1` logs the path parameter (value of `:param1`)
- On GET `/path2` or `/path3` or `/path4` log the request. Try at least 2 different types of paths.

---
# Response
- The [Response](http://expressjs.com/en/4x/api.html#res) object can be used to manipulate and send the response back
- Multiple methods available:
    - Set cookies: `res.cookie('myCookie', 'val')`
    - Send response (accepts string, object, array of Buffer): `res.send({id: 1})`
    - Send HTTP status: `res.sendStatus(200)` (same as `res.status(200).send('200')`)
    - Redirect: `res.redirect('https://google.fi')`
- Always make sure to actually send a response, e.g. `res.status(200)` will hang

---
# Exercise
- On GET `/json-response` answer with JSON `{id: 1, name: 'My response'}`
- On POST `/to-google` redirect user to `https://google.fi/` 
- On GET `/not-gonna-find` send back HTTP status 404 
- On GET `/give-me-cookie` send back cookie `for=you`
- On DELETE `/cookie-for` remove the cookie `for` and return HTTP status 200

---
# Exercise
Read the [Response documentation](http://expressjs.com/en/4x/api.html#res) and find out which method should be used to answer based on the `Accept` header. 

---
# Routers
- "A router object is an isolated instance of middleware and routes"
- Works mostly like application as you can register routes and middleware
- Missing for example view engines and `listen` method
- Can be mount under certain path:
```javascript
const router = express.Router();
router.get('/users', (req, res) => {
    res.send('Hello from router!');
});
app.use('/myApi', router);
```
Now available in `localhost:3000/myApi/users`.

---
# Exercise
Create own router and mount it to `/routed`. The router itself should respond to
- GET `/path` with HTTP status 200

---
# Middleware
- Middleware makes it possible to react to requests
- They can:
    - Execute any code
    - Make changes to the request and the response objects
    - End the request-response cycle (by using e.g. `send`)
    - Call the next middleware in the stack
- Middleware is executed in the registration order
- Middleware is registered with `use`
```javascript
app.use((req, res, next) => {
    req.started = Date.now();
    next();
});
```

---
# Chaining handlers
- `next` will trigger the next handler
```javascript
app.use((req, res, next) => {
    console.log('A');
    next();
});
app.use((req, res, next) => {
    console.log('B');
    next();
});
app.get('/foo', () => {
    console.log('C');
});
```
Logs `ABC`
- Each handler needs to call either `next` or send a response, otherwise request will hang.

---
# Mounting
Middleware can also be mounted on certain paths so it won't be ran on every request:
```javascript
app.use('/middleware', (req, res, next) => {
    console.log('Middleware used.');
    next();
});
```

---
# Example: JSON body parser
- [body-parser](https://github.com/expressjs/body-parser) implements one middleware for parsing JSON etc.
- Usage:
```javascript
const bodyParser = require('body-parser');
app.use(bodyParset.json());
```

---
# Exercise
Write your own middleware that..
- Sends HTTP status 403, if query parameter `foo` is not set to `bar`
- Stores start time of request, and then waits for one second (`setTimeout`) and then prints it

---
# Exercise
As noted earlier, each router can have its own middleware, apply middleware to the previously created router to log each request for it.

---
# Request body
- By default request body is `undefined`
- Will be populated when body parsing middleware is used
- Most usual body parsing middleware are body-parser (raw, text, JSON, etc.) and multer (_application/x-www-form-urlencoded_)

---
# Available middleware
- Express.js is compatible with most of the [Connect middleware](https://github.com/senchalabs/connect/wiki)
- There's also [some middleware](https://github.com/expressjs/express/wiki?_ga=1.21089595.1881797236.1483455596#middleware) only for Express.js
- Express.js is an extension of [Connect](https://github.com/senchalabs/connect) to include routing and template engines and they thus share most of the middleware.
- Since Express.js v4.x, it is not actually based on on Connect, but the middleware is still mostly compatible.  

---
# Serving static files
- `express.static` middleware to serve to serve static files (HTML, CSS, PDF, etc.)
- Usage:
Assuming there is `public` folder with `my.txt` inside it in the root:
```javascript
app.use(express.static('public'));
```
Files can now be accessed as `localhost:3000/my.txt`

---
# Serving static files with prefix
- To serve static files with path prefix, use the normal middleware path registration:
```javascript
app.use('public', express.static('public'));
```
resources are now available via `localhost:3000/public/my.txt`

---
# Serving static files from multiple folders
- For multiple static file folders, `express.static` middleware can be called multiple times:
```javascript
app.use(express.static('public'));
app.use(express.static('files'));
```
- If there's a file with same name, first one takes precedence (file in `public` in example)

---
# Error handling
- Calling the `next` with parameter will invoke error handler.
- Custom error handlers can be registered by providing middleware with 4 parameters:
```javascript
app.use((err, req, res, next) => {
    console.log(`Error happened: ${err}`);
});
```
- Can be chained with `next` like normal middleware handlers
- Express has default error handler which is always the last in chain

---
# Default error handling
```javascript
app.get('/error', (req, res, next) => {
    next('Random error');
});

app.use((err, req, res, next) => {
    console.error(`ERROR HAPPENED: ${err}`);
    next(`Error: ${err}`);
});
```
prints `Error: Random error`

---
# Exercise
Write your own error handler, that catches 404 and shows error message

---
# Debug mode
To see internal logging of Express.js, launch the application as:
- Windows: 
```shell
set DEBUG=express:* & node index.js
```
- Linux: 
```
DEBUG=express:* node index.js
```

---
# Exercise
Enable debug mode and find from the log generated 
- on start-up whether app is in production or development mode?
- during request, in which order are the paths matched?

---
# Catch-all route
To catch all requests that don't match any route, wildcard route (`*`) can be used:
```javascript
app.get('*', (req, res, next) => {
    next(`No matching path was found`);
});
```
sends `No matching path was found` to client.

---
# Exercise
Make a catch-all route that dispatches event to custom error handler that sends an error response.

---
# Template engines
- Allow rendering templates with parameters with template languages such as Pug and Handlebars
- To enable:
    - Install template engine: `npm install pug --save`
    - Enable the engine: `app.set('view engine', 'pug')`
    - Create `views/view1.pug` with Pug template
    - On handler, call `res.render('view1', params)`

---
# Example: Pug (formerly called Jade)
_view1.pug_
```jade
html
  head
    title= title
  body
    h1= message
```

_index.js_
```javascript
app.set('view engine', 'pug');
app.get('/view1', (req, res) => {
  res.render('view1', { title: 'Page title', message: 'Message!' });
});
```

---
# Exercise
Find out what template engines there are, pick one and use it to render. *Pug is not allowed.*

---
# Express generator
- Generator to scaffold a new Express.js project
- Usage:
```shell
npm install -g express-generator
express MY_PROJECT
cd MY_PROJECT
npm install
npm start
```
- Generates ES5 code (`var`, `function`), but ES6 support on almost ready [Pull Request](https://github.com/expressjs/generator/pull/146)
- Supports also template engines

---
# Code organization
- *Really* opinionated area
- Most common solution (?) is to divide the code as MVC ([blog post](https://www.terlici.com/2014/08/25/best-practices-express-structure.html)):
    - `controllers/`: Controllers for respond to requests
    - `models/`: Database models
    - `views/`: Views (if the application isn't just returning JSON)
    - `helpers/`: Helper utility
    - `middlewares/`: The custom middleware for the application
    - `spec/` or `tests/`: Tests with their helpers
    - `app.js` or `index.js` or `server.js`: Application main file that boots up the Express.js
