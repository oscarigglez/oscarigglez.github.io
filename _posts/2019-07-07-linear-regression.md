---
layout: post
title: Multiple linear regression from scratch
description: This post doesn't have a description (yet)
tags: python data-science stats
published: true
---


<div class="message">
  Este post sirve para tener algún contenido en el blog y poder probar los asuntos de las tags y ajustar el css y toda esa vaina. :D
</div>

$$h_\theta(x)=\theta^T x = \theta_0 x_0 + \theta_1 x_1 + \theta_2 x_2 + ... + \theta_n x_n$$

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

**Amazing coding skills.**
