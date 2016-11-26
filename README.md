# [ΔOS: Decentralized Operating System](https://www.desantis.io) | [![Build Status](https://travis-ci.org/DeSantisInc/DeOS.svg?branch=master)](https://travis-ci.org/DeSantisInc/DeOS) [![Community][badge_community]](https://desantis.im) ![License][badge_license]

> *The languages of intelligence (writing) and self-interest (money) are the*
> *mind's greatest creations; both must be decentralized or all is lost.*
> **[—DeSantis](https://twitter.com/desantis/status/795023340704595968)**

## Getting Started

### Install:

```sh
Δ git clone git@github.com:DeSantisInc/DeOS.git
```

### Run:

```sh
Δ make vm
```

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

[badge_community]: https://cdn.rawgit.com/DeSantisInc/DeOS/atd-release-v0.3-alpha/var/github/badges/community-slack.svg
[badge_license]: https://cdn.rawgit.com/DeSantisInc/DeOS/atd-release-v0.3-alpha/var/github/badges/license-bsd.svg
