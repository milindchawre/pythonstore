# Killer Utility
This utility kills processes listening on specific port.

### Preparing for Development
-----------------------------
1. Ensure pip and pipenv are installed
2. Clone repository: git clone git@github.com:example/fileops
3. cd into repository
4. Fetch development dependencies: `make install`
5. Activate virtualenv: `pipenv shell`

### Usage
---------
Pass the port number.

```
$ killer 5500
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

