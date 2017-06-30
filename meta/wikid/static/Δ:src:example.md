# `src/example.sh`

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
echo "Δ(data['a'])"
echo "Δ(data['b'])"
echo "Δ(data['c'])"
```

## Test

```yaml
a: 1
b: 2
c: 3
```
