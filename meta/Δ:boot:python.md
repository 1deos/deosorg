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

## Test

```yaml
a: 1
b: 2
c: 3
```
