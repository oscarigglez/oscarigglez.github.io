#!/bin/bash

echo "---
layout: post
title: $1
description: A new blog post
tags:
mathjax: false
published: false
---" > ./_posts/`date +%Y-%m-%d`-$1.md
