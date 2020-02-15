#/bin/sh

sed -i '' -e 's/published: false/published: true/' $1
dirs=`dirname $1`
file=`basename $1`
mv $1 $dirs/`date +%Y-%m-%d`${file:10:999}
