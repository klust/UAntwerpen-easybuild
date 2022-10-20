#! /usr/bin/env bash

cd ..

last_group='.'

echo -e "# Package list\n"

for readme in $(ls -1 ../easybuild/easyconfigs/*/*/README.md | sort -f)
do
	
	>&2 echo "Processing $readme..." 
	
	# Remove the known part of the path and the known filename.
	work=${readme##.*easyconfigs/}
	work=${work%%/README.md}
	
	# Extract the first letter and the name of the package.
	package=${work##[0-9a-z]/}
	group=${work%%/$package}
	
	>&2 echo "Identified group $group, package $package"
	
    [[ $group != $last_group ]] && echo -e "## $group\n"
    last_group="$group"
    
    echo -e "-   $package\n"
	
done
