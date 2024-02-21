# cURL/s
> The command-line alternative to Postman

`curls` is a drop in replacement for `curl`, with state added on (the "s" is for "save"). Create and share API collections, give your curls memorable nicknames to call them up by, and more.

## Installation
```bash
$ brew install ptbrodie/curls/curls
```

## Usage

```bash
$ curls -XPOST https://api.example.com/api/v1/example -H 'content-type: application/json' -d '{"some": {"data": "here"}}'

$ curls history
+History---------------------------+------+---------------------+------------------------------------------------------------------------+
| id                               | name | date                | command                                                                |
+----------------------------------+------+---------------------+------------------------------------------------------------------------+
| 350f41c5a89a485187649931dbb4c6b5 | -    | 2024-02-21 19:35:30 | $ curls -XPOST https://api.example.com/api/v1/example -H 'content-type:|
|                                  |      |                     | application/json' -d '{"some": {"data": "here"}}'                      |
+----------------------------------+------+---------------------+------------------------------------------------------------------------+
```

## Naming and using curls

Every curl you run with `curls` is saved and given a unique id by default. You can reference the curl by its id or give it a human-readable name.

```bash
# Rerun an old curl
$ curls 350f41c5a89a485187649931dbb4c6b5 

# Give a curl a name
$ curls name 350f41c5a89a485187649931dbb4c6b5 'my-curl'
$ curls history 
+History---------------------------+---------+---------------------+------------------------------------------------------------------------+
| id                               | name    | date                | command                                                                |
+----------------------------------+---------+---------------------+------------------------------------------------------------------------+
| 350f41c5a89a485187649931dbb4c6b5 | my-curl | 2024-02-21 19:35:30 | $ curls -XPOST https://api.example.com/api/v1/example -H 'content-type:|
|                                  |         |                     | application/json' -d '{"some": {"data": "here"}}'                      |
+----------------------------------+---------+---------------------+------------------------------------------------------------------------+

# Give a curl a description
$ curls describe my-curl "This is a description of my curl."
$ curls info my-curl

ID: 350f41c5a89a485187649931dbb4c6b5
Date: 2024-02-21 19:35:30
Name: my-curl
Description: This is a description of my curl.
Command: curls -XPOST https://api.example.com/api/v1/example -H 'content-type: application/json' -d '{"some": {"data": "here"}}'
```

## Creating and Managing APIs
An API is a curated collection of curls. Use APIs for storing a collection of tests, or complex curls you don't want to re-type, or curating a collection of curls to share with a colleague.
```bash
# View APIs
$ curls api
  default
* existing-api

# Create new API
$ curls api create 'new-api'
$ curls api
  default
* existing-api
  new-api

# Switch to the new API
$ curls use new-api
$ curls api
  default
  existing-api
* new-api

# Add a cURL to an API
$ curls add 350f41c5a89a485187649931dbb4c6b5
$ curls
+new-api---------------------------+------+---------------------+------------------------------------------------------------------------+
| id                               | name | date                | command                                                                |
+----------------------------------+------+---------------------+------------------------------------------------------------------------+
| 350f41c5a89a485187649931dbb4c6b5 | -    | 2024-02-21 19:35:30 | $ curls -XPOST https://api.example.com/api/v1/example -H 'content-type:|
|                                  |      |                     | application/json' -d '{"some": {"data": "here"}}'                      |
+----------------------------------+------+---------------------+------------------------------------------------------------------------+

# Remove a cURL from an API
$ curls remove 350f41c5a89a485187649931dbb4c6b5
$ curls
+new-api-+-------+---------+-----------+
| id     | name  | date    | command   |
+--------+-------+---------+-----------+
```

## Sharing Your APIs

```bash
# Export an API to a json file.
[mine] $ curls export shared-api
API exported to shared-api.json.

# Import an API from a json file.
[yours] $ curls import shared-api.json
[yours] $ curls api
* default
  shared-api
[yours] $ curls use shared-api
```





