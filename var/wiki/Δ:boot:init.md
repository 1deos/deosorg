# `boot/init.lz`

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
UPDATE && UPGRADE
INSTALL "build-essential"
INSTALL "clang"
INSTALL "llvm"
INSTALL "libffi-dev"
INSTALL "libssl-dev"
INSTALL "git"
INSTALL "curl"
INSTALL "apt-transport-https"
INSTALL "ca-certificates"
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

