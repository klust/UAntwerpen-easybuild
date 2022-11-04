#! /usr/bin/env bash

# That cd will work if the script is called by specifying the path or is simply
# found on PATH. It will not expand symbolic links.
cd $(dirname $0)
cd ..
docdir=$(PWD)
cd ..
repodir=$(PWD)

#
# Set some variables that will be used as constants
#
gendoc='generated'
userinfo='USER.md'

################################################################################
#
# Main code
#

#
# Set up the structure.
#

cd $docdir
[[ -d $gendoc ]] || mkdir $gendoc
cd $gendoc

/bin/cp -f ../config/mkdocs.tmpl.yml mkdocs.yml
echo -e "\nnav:" >>mkdocs.yml

mkdir -p docs
/bin/cp -r ../stylesheets docs/stylesheets

package_list='docs/index.md'

last_group='.'

echo -e "---\ntitle: Package overview\nhide:\n- navigation\n---\n" >$package_list
echo -e "# Package list\n" >>$package_list

# Note that we deliberately use relative references in the ls call below.
#for package_dir in $(/bin/ls -1 ../../easybuild/easyconfigs/y/*/*.eb | sed -e 's|.*/easyconfigs/\(.*/.*\)/.*\.eb|\1|' | sort -uf)
for package_dir in $(/bin/ls -1 ../../easybuild/easyconfigs/*/*/*.eb | sed -e 's|.*/easyconfigs/\(.*/.*\)/.*\.eb|\1|' | sort -uf)
do
	
	>&2 echo "Processing $package_dir..." 
	
	# Extract the first letter and the name of the package.
	package=${package_dir##[0-9a-z]/}
	group=${package_dir%%/$package}
	
	>&2 echo "Identified group $group, package $package"

	mkdir -p docs/$package_dir
	package_file="docs/$package_dir/index.md"

    # Create the package file.

	echo -e "---\ntitle: $package\nhide:\n- navigation\n---\n" >$package_file

    echo -e "[[package list]](../../index.md)\n" >>$package_file
	echo -e "# $package\n" >>$package_file

	#
	# Generate the user documentation if a USER.md file exists.
	#
    usage="../../easybuild/easyconfigs/$package_dir/$userinfo"
	if [[ -f $usage ]]
    then
	    echo -e "## User documentation\n" >>$package_file
		egrep -v "^# " $usage | sed -e 's|^#|##|' >>$package_file
	fi

    #
	# Generate a list of EasyConfig files
	#

	echo -e "## Available EasyConfigs\n" >>$package_file

    prefix="../../easybuild/easyconfigs/$package_dir"
	for file in $(/bin/ls -1 $prefix/*.eb | sort -f)
	do

        easyconfig="${file##$prefix/}"
		easyconfig_md="docs/$package_dir/${easyconfig/.eb/.md}"

		>&2 echo "Processing $easyconfig, generating $easyconfig_md..."

        echo -e "---\ntitle: $easyconfig - $package\nhide:\n- navigation\n- toc\n---\n" >$easyconfig_md
        echo -e "[[$package]](index.md) [[package list]](../../index.md)\n" >>$easyconfig_md
        echo -e "# $easyconfig\n" >>$easyconfig_md
		echo -e '``` python' >>$easyconfig_md
		cat $file >>$easyconfig_md
		echo -e '\n```\n' >>$easyconfig_md
        echo -e "[[$package]](index.md) [[package list]](../../index.md)" >>$easyconfig_md
        # Note the extra \n in front of the last ``` as otherwise files that do not end
        # with a newline would cause trouble.

		echo -e "-    [$easyconfig](${easyconfig/.eb/.md})" >>$package_file

	done

	#
	# Generate the techical documentation if a README.md file exists.
	#
    readme="../../easybuild/easyconfigs/$package_dir/README.md"
	if [[ -f $readme ]]
    then
	    echo -e "## Technical documentation\n" >>$package_file
		egrep -v "^# " $readme | sed -e 's|^#|##|' >>$package_file
	fi

    #
	# Finish the package list
	#
    echo -e "\n[[package list]](../../index.md)" >>$package_file

    # If this is a new group, add the letter to the navigation menu.

    [[ $group != $last_group ]] && echo "- $group: index.html#$group" >>mkdocs.yml

	# Finally add the link to the package list

    [[ $group != $last_group ]] && echo -e "## $group\n" >>$package_list
    last_group="$group"
    
    echo -e "-   [$package](${package_file#docs/})\n" >>$package_list
	
done
