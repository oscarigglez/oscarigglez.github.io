---
layout: post
title: A pair of useful scripts
description: Two simple shell scripts that help me manage my blog
tags: blog scripts
mathjax: false
published: false
---

This blog, having been built on the wonderful Jekyll template called Hyde, has quite a neat method for adding new content: I just need to create a new Markdown file in the posts directory and include the publication date in its name using the following format ```YYYY-MM-DD-whatever.md```.
Then, I type a little YAML heading with its layout type, a title, a description... and it's all set up!

Simple enough, right?

The following shell script simplifies this even further by automating it: I just type the name that I wanna give to my post, and a properly formatted file is generated and opened for me to type to my heart's desires.

```new_post.sh```
```bash
#!/bin/sh

filename=./_posts/`date +%Y-%m-%d`-$1.md # generates a name with the current date
content="---\nlayout: post\ntitle: $1\ndescription: A new blog post\ntags:\nmathjax: false\npublished: false\n---" # YAML heading
test -f $filename || echo $content > $filename # if the file doesn't exist, makes a new one
vim $filename # opens the file for inmediate editing
```

Writing blog posts is not always easy or straightforward, though, and rare is the ocassion where I finish one the same day that I start it. What if I complete a blog post, I want to publish it, and the date is all wrong? The steps couldn't be easier: I just need to change its filename to one with the current date, and change the value of the ```published``` field in the YAML field to ```true```. Again, this is quite straightforward as it is, but I've also written a small bash script to do it all in one step because... well, because I'm kind of lazy!

```publi.sh```
```bash
#/bin/sh

sed -i '' -e 's/published: false/published: true/' $1 # changes the published field
dirs=`dirname $1`
file=`basename $1`
mv $1 $dirs/`date +%Y-%m-%d`${file:10:999} # changes the filename to have the current date
```
