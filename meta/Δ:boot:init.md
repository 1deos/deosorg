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
#!/bin/sh
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
