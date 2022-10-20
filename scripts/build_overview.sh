#! /usr/bin/env bash

cd ..
[[ -d generated ]] || mkdir generated
cd generated
[[ -h easyconfigs ]] || ln -s ../../easybuild/easyconfigs

package_list='package_list.md'

last_group='.'

echo -e "# Package list\n" > $package_list

for readme in $(ls -1 easyconfigs/*/*/README.md | sort -f)
do
	
	>&2 echo "Processing $readme..." 
	
	# Remove the known part of the path and the known filename.
	work=${readme##easyconfigs/}
	package_dir=${work%%/README.md}
	
	# Extract the first letter and the name of the package.
	package=${package_dir##[0-9a-z]/}
	group=${package_dir%%/$package}
	
	>&2 echo "Identified group $group, package $package"

	mkdir -p $package_dir
	package_file="$package_dir/package.md"

    # Create the package file.

	echo -e "# $package\n" >$package_file

	[[ -f "$readme" ]] && echo -e "-   [Technical documentation](../../$readme)\n" >>$package_file

	# Finally add the link to the package list

    [[ $group != $last_group ]] && echo -e "## $group\n" >>$package_list
    last_group="$group"
    
    echo -e "-   [$package]($package_file)\n" >>$package_list

	
done
