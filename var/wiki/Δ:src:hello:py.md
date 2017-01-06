# `src/hello.py`

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

```python
Δ with (data=None)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

def main():
    print('hello, world!')

if __name__=="__main__":
    main()
```

## Test

```yaml
a: 1
b: 2
c: 3
```
