# HR Utility

This utility:
- Received a list of user dictionaries and ensure that the system’s users match.
- Have a function that can create a user with the given information if no user exists by that name.
- Have a function that can update a user based on a user dictionary.
- Have a function that can remove a user with a given username.
- The create, update, and remove functions should print that they are creating/updating/removing the user before executing the command.

The user information will come in the form of a dictionary shaped like this:
```
    {
      'name': 'kevin',
      'groups': ['wheel', 'dev'],
      'password': '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'
    }
```

### Preparing for Development
-----------------------------
1. Ensure pip and pipenv are installed
2. Clone repository: git clone git@github.com:example/hr
3. cd into repository
4. Fetch development dependencies: `make install`
5. Activate virtualenv: `pipenv shell`

### Usage
---------
Adding, Removing, Updating users in linux:
```
$ hr path/to/inventory.json
Adding user 'john'
Added user 'john'
Updating user 'scott'
Updated user 'scott'
Removing user 'lina'
Removed user 'lina'
```

Export current linux users state in inventory file.
```
hr --export path/to/inventory.json
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

