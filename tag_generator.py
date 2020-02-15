#!/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os

post_dir = '_posts/'
tag_dir = 'tag/'
tagindex_dir = 'tagindex/'

filenames = glob.glob(post_dir + '*md')


# Retrieve the unique tags from all of the blog posts
total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)


# Remove old and unused tag and tagindex pages
old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

old_tags = glob.glob(tagindex_dir + '*.md')
for tag in old_tags:
    os.remove(tag)


# Creates the tag/ and tagindex/ directories if they don't exist
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

if not os.path.exists(tagindex_dir):
    os.makedirs(tagindex_dir)


for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nmathjax: true\nrobots: noindex\n---\n'
    with open(tag_filename, 'a') as f:
        f.write(write_str)

    tagindex_filename = tagindex_dir + tag + '.md'
    write_str = '---\nlayout: tagindexpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    with open(tagindex_filename, 'a') as f:
        f.write(write_str)

print("Tags generated, count", total_tags.__len__())
