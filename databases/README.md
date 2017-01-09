# Databases
- Databases nowadays
- MongoDB in general
- Mongoose

---
# Databases nowadays
- Databases available for general and specialized use cases
- Relational vs. NoSQL
- NoSQL is extremely wide term as it contains at least:
    - Document databases like MongoDB
    - Key-value storages like Redis
    - Graph databases like OrientDB and Neo4j
    - Object databases
    - Tabular databases like Hbase and BigTable

---
# MongoDB in general
- Free & [open-source](https://github.com/mongodb/mongo) document-oriented database (NoSQL)
- Initially released 2009, currently on v3

---
# Main features
- Ad hoc queries
- Indexing
- High availability (replication)
- Supports sharding (scaling horizontally)
- File storage
- JavaScript execution
- Aggregation with map-reduce

---
# Basic structure
- Server has multiple _databases_
- Database has multiple _collections_ (tables in relational world)
- Collection has multiple _documents_ (rows)
- Document has multiple _fields_ (columns)

---
# Collections
- Like tables in relational terminology
- Usually contains many, related documents
- Do not enforce schema on documents
- Starting from 3.2 validations available for documents (checked on inserts and updates)

---
# Documents
- JSON-like structure for collection of key-value pairs
- Serialized and stored actually as BSON (Binary JSON)
- Can have different fields from each other within the collection
- Collection-wide unique `ObjectId` (12-byte, stored usually in `_id`) can be manually set for document. If not set, one is generated

---
# Modeling data
- Modeling the data is different from relational databases
- Key concept: Storage is cheap compared to computing time, duplicating data is okay
- Model data by user requirements
- Joins on write, not on read
- Optimize for most usual use case
- Example: Blog post documents stores tags (strings) and comments (objects with text, author etc.) within the document

---
# Mongoose
- MongoDB object modeling for Node.js
- Provides a schema-based solution to model data
- Built-in type casting, validation, query building, business logic hooks etc.

---
# Connecting
- Connecting is simple:

```javascript
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/test').then(() => {
    console.log('Connected successfully.');
});
```
- In case connection is lost, Mongoose automatically reconnects and executes all commands in buffer
- Format for URL is: `mongodb://[username:password@]host1[:port1][/[database]]`

---
# Schemas
- Declares the shape of data for certain collection
- Example:

```javascript
const Schema = mongoose.Schema;

const blogSchema = new Schema({
  title:  String,
  author: String,
  body:   String,
  comments: [{ body: String, date: Date }],
  date: { type: Date, default: Date.now },
  hidden: Boolean,
  meta: {
    votes: Number,
    favs:  Number
  }
});
```

---
# SchemaTypes
- Available SchemaTypes are:
    - String
    - Number
    - Date
    - Buffer
    - Boolean
    - Mixed
    - ObjectId
    - Array

---
# Models
- To use schema, we need to create a model with the schema specified with `mongoose.model(modelName, schema)`:

```javascript
const Blog = mongoose.model('Blog', blogSchema);
```
- Each instance of model is a document

---
# Instance methods
- Models have some built-in instance methods
- Models can also have custom instance methods:

```javascript
blogSchema.methods.findFromSameDate = (cb) => {
  return this.model('Blog').find({ date: this.date }, cb);
};
var post1 = new Blog({ date: Date.now(), ... });

post1.findFromSameDate((err, posts) => {
  console.log(posts); // woof
});
```
- Built-in instance methods should not be overwritten

---
# Static methods
- Can be used for example to perform more sophisticated lookups:

```javascript
blogSchema.statics.findByTitle = (title, cb) => {
  return this.find({ title: new RegExp(title, 'i') }, cb);
};

Blog.findByTitle('My title', (err, posts) => {
  console.log(posts);
});
```

---
# Query helpers
- Query helpers allow chained query building:

```javascript
blogSchema.query.byTitle = (title) => {
  return this.find({ title: new RegExp(title, 'i') });
};

Blog.find().byTitle('My title').exec((err, posts) => {
  console.log(posts);
});
```

---
# Promises
- All async operations return promises
- Queries do return object with `.then()` but are not actual fully-fledged promises (use `.exec()` to obtain one)
- For backwards-compatibility reasons, Mongoose returns [mpromise](https://www.npmjs.com/package/mpromise) promises by default
- Can be changed to more modern solutions such as native ES6 promises:

```javascript
mongoose.Promise = global.Promise; // ES6 promises
mongoose.Promise = require('q').Promise; // q library promises
```
