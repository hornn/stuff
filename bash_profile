
PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/local/bin:/opt/local/sbin
PATH=$PATH:/usr/local/git/bin:
export M2_HOME=/Applications/apache-maven-3.2.3
PATH=$PATH:$M2_HOME/bin
# Set Perl 5.12 for GPDB/HAWQ
export PERLHOME=/opt/tools_build/tools/perl/5.12.4/dist/osx105_x86/perl-5.12.4
#export PERLHOME=/Users/nhorn/dev/hornn_mac2/tools/perl/5.12.4/dist/osx105_x86/perl-5.12.4
export PATH=$PERLHOME/bin:$PATH
export PERL5LIB=$PERLHOME/lib/5.12.4

 #Perforce definitions:
export P4USER=hornn
export P4CONFIG=.p4config
export P4PORT=perforce.greenplum.com:1666
export P4EDITOR=vi

# Useful aliases:
alias ll="ls -l"
alias jps="jps | sort -k 2"
alias bt="/Users/nhorn/scripts/beep_test.sh"
alias gprestart="gpstop -a && sleep 5 && gpstart -a && bt"
alias p4diff="/Applications/p4merge.app/Contents/MacOS/p4merge"
alias gotoreg="cd apache-hawq/src/test/regress/"
function diffreg()
{
if [[ "x$1" == "x" ]]; then
echo "Usage: diffreg <regression test name>"
return 1
fi
gotoreg
p4diff expected/$1.out results/$1.out &
cd -
}

# kill postgres remains:
alias killpostgres='killall postgres; ipcclean; rm -f /tmp/.s*'

function maxof()
{
re='^[0-9]+$'
if ! [[ $1 =~ $re ]]; then
echo "Usage: maxof <open files threshold>"
return 1
fi
pids=`ps -ef | awk '{print $2}' | grep -v PID`; 
for i in $pids; do 
	b=$(lsof -p $i | wc -l) ; 
	if [[ $b -gt $1 ]]; then 
		p=$(ps -p $i);
		echo $b, $i, $p; 
	fi; 
done | sort -n
}

function dbdump()
{
if [[ "x$1" == "x" ]]; then
	echo "Usage: dbdump <db name>"
	echo ""
	echo "Hint: run psql -l to get the list of databases:"
	psql -l
	return 1
fi
dest=$GPDATA/$1.sql
pg_dump -s $1 > $dest
if [[ $? -ne 0 ]]; then
	echo dbdump failed!
	return 1
fi
echo db schema $1 saved into $dest 
}

# vm 
alias ssh_vm="ssh hornn@vm-centos64"
alias sethostname="sudo scutil --set HostName nhorn-mbp && hostname"

##################
#JAVA/HADOOP stuff
##################
# this is the java_home indicated by running /usr/libexec/java_home
#export JAVA_HOME=/Library/Java/Home
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_72.jdk/Contents/Home
export PATH=${JAVA_HOME}/bin:$PATH

# hadoop conf, single cluster 1.2
#export HADOOP_ROOT=/Users/hornn/single_cluster/single_cluster-1.0-gphd-1.2/hadoop
#export HBASE_ROOT=/Users/hornn/single_cluster/single_cluster-1.0-gphd-1.2/hbase
#export ZOOKEEPER_ROOT=/Users/hornn/single_cluster/single_cluster-1.0-gphd-1.2/zookeeper
#export SINGLE_CLUSTER_ROOT=/Users/hornn/single_cluster/single_cluster-1.0-gphd-1.2

# hadoop conf, single cluster 2.0
#export SINGLE_CLUSTER_ROOT=/Users/hornn/single_cluster/single_cluster-1.5a-gphd-2x
#export HADOOP_ROOT=${SINGLE_CLUSTER_ROOT}/hadoop
#export HBASE_ROOT=${SINGLE_CLUSTER_ROOT}/hbase
#export ZOOKEEPER_ROOT=${SINGLE_CLUSTER_ROOT}/zookeeper
#export HIVE_ROOT=${SINGLE_CLUSTER_ROOT}/hive

export GPHD_ROOT=/Users/nhorn/single_cluster/singlecluster-PHD-3.3
#export GPHD_ROOT=/Users/nhorn/single_cluster/singlecluster-PHD-16178
export HADOOP_ROOT=$GPHD_ROOT/hadoop
export HBASE_ROOT=$GPHD_ROOT/hbase
export HIVE_ROOT=$GPHD_ROOT/hive
export ZOOKEEPER_ROOT=$GPHD_ROOT/zookeeper
export PATH=$PATH:$GPHD_ROOT/bin:$HADOOP_ROOT/bin:$HBASE_ROOT/bin:$HIVE_ROOT/bin:$ZOOKEEPER_ROOT/bin


# init db
#alias dbrefresh='CURPATH=$PWD; cd ~/gpsql-data/ ; ./gp_remove_11000; gpinitsystem -c gpsql_init_config -a; cd $CURPATH'

# beep test:
function beep_test()
{

$*
echo -e "Done!" "\a" "\a" "\a"
#echo "Done testing" "\007" "\007" "\007" # beep beep beep

}

# buildme:
function buildme()
{
if [ "x$GPROOT" == "x" ]; then
	echo GPROOT undefined!
	exit 1
fi
distpath=$GPROOT
build_output=`cd $distpath;pwd`
#make HOME=$build_output $*
make DEVPATH=`cd $GPHOME;pwd` $*
#make -f build-utils/pivotal/Makefile HOME=`cd $GPHOME;pwd` $*
#make -f build-utils/pivotal/Makefile DEVPATH=`cd $GPHOME;pwd` $*
}

# Greenplum environment definitions:
#alias getgit="echo `git branch | grep '*' | awk '{print $2}'`" 
alias getgit="git branch | sed -n '/\* /s///p'"

alias gphere='set_greenplum_project `pwd` `getgit`'

function set_greenplum_project()
{

source /opt/gcc_env-osx106.sh
export PGPORT=5432 
export PGHOST="127.0.0.1"

local DIST_ROOT=~/Projects/gp/dist
# verify we have an argument
if [[ "x$1" == "x" || "x$2" == "x" ]]; then
echo "Usage: $0 <greenplum build path> <git branch>"
return 1
fi

export BUILD_ROOT=$1

# verify BUILD_ROOT is a valid gpdb build path
if [[ ! -d $BUILD_ROOT/cdb-pg && ! -d $BUILD_ROOT/build-utils ]]; then
echo $BUILD_ROOT is not a valid build directory
return 1
fi

echo $BUILD_ROOT | grep "/Users/nhorn/dev" 
if [[ $? -ne 0 ]]; then
echo $BUILD_ROOT is not a valid build directory
return 1
fi

local PROJECT_NAME=`echo $BUILD_ROOT | sed 's/\/Users\/nhorn\/dev\///' | sed 's/hornn_mac2\///' | sed 's/\//_/g'`
echo $PROJECT_NAME

local GIT_NAME=$2
echo $GIT_NAME

# sed script which removes all subpaths (delimited by ':') containing hawq-db-devel
local VARCLEANUP_SCRIPT='s|[[:alnum:]/_-]*hawq-db-devel[[:alnum:]/_-]*:||g'

# cleanup environment
unset OPENSSL_CONF
unset PYTHONPATH
unset PYTHONHOME
export PATH=`echo $PATH | sed -E $VARCLEANUP_SCRIPT`
export DYLD_LIBRARY_PATH=`echo $DYLD_LIBRARY_PATH | sed -E $VARCLEANUP_SCRIPT`
unset GPHOME
unset GPDATA
unset MASTER_DATA_DIRECTORY

# setup environment
export GPROOT=$DIST_ROOT/$PROJECT_NAME/$GIT_NAME
export GPDATA=$GPROOT/gp-data
export GPHOME=$GPROOT/greenplum-db-devel
export MASTER_DATA_DIRECTORY=$GPDATA/master/gpseg-1

if [[ ! -d $GPROOT || ! -d $GPDATA || ! -d $GPHOME ]]; then
mkdir -p $GPROOT
mkdir -p $GPDATA
mkdir -p $GPHOME
fi

local GPENV_FILE=$GPHOME/greenplum_path.sh

if [ -f $GPENV_FILE ]; then
source $GPENV_FILE
fi

if [ -f $BUILD_ROOT/hawq-db-devel/greenplum_path.sh ]; then
source $BUILD_ROOT/hawq-db-devel/greenplum_path.sh
fi
#if [ -f $BUILD_ROOT/hawq-db-dist/greenplum_path.sh ]; then
#source $BUILD_ROOT/hawq-db-dist/greenplum_path.sh
#fi

export PYTHONPATH=/Library/Python/2.6/site-packages:$PYTHONPATH


export HADOOP_HOME=$HADOOP_ROOT

if [[ $PROJECT_NAME =~ 'gpdb' ]]; then
export JAVA_HOME=/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
export PATH=${JAVA_HOME}:$PATH
echo $JAVA_HOME
fi

}

alias rm_libxml='rm -f $GPHOME/lib/libxml*'

alias cp_conf='cp $GPDATA/hawq-site.xml $GPDATA/slaves $GPHOME/etc/.'

alias gitundo='git reset --soft HEAD~1'

function chpxfjar()
{
for i in {service,api,hdfs,hive,hbase}; do 
  echo $i; 
  rm pxf-$i.jar; 
  ln -s pxf-$i-3.0.0.jar pxf-$i.jar; 
done
} 

##
# Your previous /Users/hornn/.bash_profile file was backed up as /Users/hornn/.bash_profile.macports-saved_2014-03-09_at_19:21:23
##

# MacPorts Installer addition on 2014-03-09_at_19:21:23: adding an appropriate PATH variable for use with MacPorts.
# export PATH=/opt/local/bin:/opt/local/sbin:$PATH
# Finished adapting your PATH environment variable for use with MacPorts.

export PATH="$PATH:/Applications/HP_Fortify/HP_Fortify_SCA_and_Apps_4.30/bin"

# Setting PATH for MacPython 2.6
# The orginal version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/2.6/bin:${PATH}"
export PATH
