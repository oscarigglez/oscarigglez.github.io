---
layout: post
title: Python test
description: Esta es... otra descripción. :o
tags: chemistry python
mathjax: true
published: false
---


<div class="message">
  Este post sirve para tener algún contenido en el blog y poder probar los asuntos de las tags y ajustar el css y toda esa vaina. :D
</div>

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
