# [ΔOS: Decentralized Operating System](https://www.desantis.io) | [![Build Status](https://travis-ci.org/DeSantisInc/DeOS.svg?branch=master)](https://travis-ci.org/DeSantisInc/DeOS)

> *The languages of intelligence (writing) and self-interest (money) are the*
> *mind's greatest creations; both must be decentralized or all is lost.*
> **[—DeSantis](https://twitter.com/desantis/status/795023340704595968)**

## Getting Started

### Install:

#### 1. Clone the Repo:

```sh
Δ git clone git@github.com:DeSantisInc/DeOS.git
```

#### 2. Install Vagrant:

```sh
Δ brew cask install vagrant
```

#### 3. Install Virtualbox:

```sh
Δ brew cask install virtualbox
```

#### 4. Install the Virtual Machine:

```sh
Δ make vm
```

#### 5. Connect to the Virtual Machine:

```sh
Δ make sh
```

#### 6. Shutdown the Virtual Machine:

```sh
Δ make rm
```

### Known Issues

If you encounter an error message like below:

```
==> DeVM: Box 'ubuntu/trusty64' could not be found. Attempting to find and install...
    DeVM: Box Provider: virtualbox
    DeVM: Box Version: >= 0
The box 'ubuntu/trusty64' could not be found or
could not be accessed in the remote catalog. If this is a private
box on HashiCorp's Atlas, please verify you're logged in via
`vagrant login`. Also, please double-check the name. The expanded
URL and error message are shown below:

URL: ["https://atlas.hashicorp.com/ubuntu/trusty64"]
Error:
```

Try the solution here: http://stackoverflow.com/a/40521433

---
