---
layout: post
title: Hello world!
description: Hi everybody! Just a little message to anyone that visits before I actually upload any interesting content.
tags: personal meta
mathjax: true
published: true
---


Hi there!

I'm still setting up the quite minimalistic features of this pretty blog, but I already have many interesting projects in mind (some of them already completed and just waiting to be properly shared).
We'll learn about programming, about math, about chemistry, about art... Stay tuned!

And now, some little tests I need to add in order to check that everything works and looks as I want it to!

_Are the images working?_

<p class="full-width">
<a href="/public/img/leaf-man.jpg" class="image">
<img src="/public/img/leaf-man.jpg" alt="" /></a>
</p>

![leaf man](/public/img/leaf-man.jpg)

[leaf man](/public/img/leaf-man.jpg)

_Are the video links working?_

[video link](https://youtu.be/iWowJBRMtpc?t=90s)

_Is the math working?_

$$h_\theta(x)=\theta^T x = \theta_0 x_0 + \theta_1 x_1 + \theta_2 x_2 + ... + \theta_n x_n$$

_Is the code highlighting working?_

```python
class System:
    def __init__(self, filename, mol_atoms):
        self.filename = filename
        self.id = str(filename[:-4])

        with open(filename, 'r') as readfile:
            self.lines = readfile.readlines()

        self.wavenumber_list = []
        for i in range(len(self.lines)):
            if "Frequencies" in self.lines[i]:
                self.wavenumber_list += self.lines[i].split()[2:]
            else:
                pass
```

Nice!
