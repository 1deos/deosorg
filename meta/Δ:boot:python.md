# `boot/python.lz`

## Schema

```yaml
type: object
required: [a, b, c]
properties:
  a: {type: number}
  b: {type: number}
  c: {type: number}
```

## Environment

```yaml
a: 1
b: 2
c: 3
```

## Template

```sh
Δ with (data=None)

MAINTAINER "atd@gmx.it"
INSTALL "python2.7"
INSTALL "python-dev"
INSTALL "python-pip" && UPGRADE_PIP
PIP_INSTALL "ndg-httpsclient"
PIP_INSTALL "pyasn1"
PIP_UPGRADE "requests[security]"
PIP_INSTALL "virtualenv"
RUN "cd /deos/venv/linux/ && virtualenv default --no-site-packages"
EXIT_SUCCESS
```

## Test: Environment

```yaml
a: 1
b: 2
c: 3
```

## Test: Pass

```sh
#!/bin/sh
echo "1"
echo "2"
echo "3"
```

## Test: Fail

```sh
#!/bin/sh
echo "3"
echo "2"
echo "1"
```

