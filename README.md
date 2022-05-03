<p align="center">
  <img src="./vsign.jpg" />
</p>

# .vsign

A Version signing library written by the VSI (Version Sign Institution).

```py

import vsign

myvs = vsign.VSign(
    "https://api.github.com/repos/thekaigonzalez/NFyMono/releases/latest", # add a url (for example, NFy Mono's latest version.)
    "https://github.com/thekaigonzalez/NFyMono/releases") # The website that will be linked when it is not up to date.

assert(myvs.validate_vsign())

myvs.set_spec("v3")

myvs.compare_vsign()

```