# Urlgetter
This utility downloads contents from a url to a given destination file.

### Preparing for Development
-----------------------------
1. Ensure pip and pipenv are installed
2. Clone repository: git clone git@github.com:example/urlgetter
3. cd into repository
4. Fetch development dependencies: `make install`
5. Activate virtualenv: `pipenv shell`

### Usage
---------
Pass url, destination file and an optional type flag to specify response type (HTML or JSON).

```
$ urlgetter url --file/-f somefile.txt --type HTML/JSON
```

### Running Tests
-----------------
Run tests locally using make if virtualenv is active:

```
$ make
```

If virtualenv isn’t active then use:

```
$ pipenv run make
```

