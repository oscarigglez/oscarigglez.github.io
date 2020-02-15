#!/bin/sh

filename=./_posts/`date +%Y-%m-%d`-$1.md
content="---\nlayout: post\ntitle: $1\ndescription: A new blog post\ntags:\nmathjax: false\npublished: false\n---"
test -f $filename || echo $content > $filename
