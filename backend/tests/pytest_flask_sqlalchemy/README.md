Local copy of the [pytest-flask-sqlalchemy](https://github.com/jeancochrane/pytest-flask-sqlalchemy), due to the [SQLAlchemy 1.3](https://github.com/jeancochrane/pytest-flask-sqlalchemy/issues/14) incompatibilty.

Changing the

```
engine.contextual_connect.return_value = connection
```

to

```
engine._contextual_connect.return_value = connection
```

helps to fix the issue, so using that for now, until the official fix arrives.
