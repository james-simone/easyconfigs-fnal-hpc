#! /bin/bash

export LMOD_IGNORE_CACHE=1
INSTALL_PATH=/srv/software/el8/x86_64/eb
module use /srv/software/el8/x86_64/hpc/lmod/Core
module use $INSTALL_PATH/lmod/all
module load easybuild

export EASYBUILD_PREFIX=/srv/software/el8/x86_64/eb/build
export XDG_CONFIG_HOME=$EASYBUILD_PREFIX/config  # "home" config files
export EASYBUILD_CONFIGFILES=$EASYBUILD_PREFIX/easyconfigs-fnal-hpc/ebconfig/config_lq.cfg
#export XDG_CONFIG_DIRS=  # other config files
export EASYBUILD_BUILDPATH=/scratch/simone/easybuild/build
export EASYBUILD_SOURCEPATH=/scratch/simone/easybuild/sources
export EASYBUILD_CONTAINERPATH=/scratch/simone/easybuild/containers
export EASYBUILD_REPOSITORYPATH=/scratch/simone/easybuild/ebfiles_repo
export EASYBUILD_INSTALLPATH_SOFTWARE=$INSTALL_PATH
export EASYBUILD_INSTALLPATH_MODULES=$INSTALL_PATH/lmod
export EASYBUILD_ROBOT_PATHS=$EASYBUILD_PREFIX/easyconfigs-fnal-hpc/lq/el8
export EASYBUILD_EXTERNAL_MODULES_METADATA=$EASYBUILD_PREFIX/easyconfigs-fnal-hpc/lq/el8/\*.cfg
export EASYBUILD_INCLUDE_MODULE_NAMING_SCHEMES=$EASYBUILD_PREFIX/easyconfigs-fnal-hpc/lmod/LowerFlatMNS.py
