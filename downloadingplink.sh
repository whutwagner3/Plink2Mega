get_input(){

usage="Usage: sh downloadingplink.sh -[OPTIONS]
	Downloads plink for OSX or Linux 
		-o : operating system, 'osx' (default) or 'linux' 
		-h : Print usage instructions" 
op="osx"
while getopts "ho:" option; do
	case $option in
		o) op=$OPTARG;;
		h) echo "$usage"
		   exit 0;;
		\?) echo "Invalid option."
			"$usage"
			exit 0;;
	esac
done

if [ "$op" == "linux" ]; then
	wget http://zzz.bwh.harvard.edu/plink/dist/plink-1.07-x86_64.zip
	unzip plink-1.07-x86_64.zip
	rm -f plink-1.07-x86_64.zip
	cp plink-1.07-x86_64/plink .
elif [ "$op" == "osx" ]; then
	wget http://zzz.bwh.harvard.edu/plink/dist/plink-1.07-mac-intel.zip
	unzip plink-1.07-mac-intel.zip
	rm -f plink-1.07-mac-intel.zip
	cp plink-1.07-mac-intel/plink .
else
	echo "invalid -o flag. Use either 'linux' or 'osx'"
fi
}

get_input "$@"
