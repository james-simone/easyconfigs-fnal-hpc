#! /bin/bash

export LMOD_IGNORE_CACHE=1
INSTALL_PATH=/srv/software/el8/ppc64le/eb
module use /srv/software/el8/ppc64le/hpc/lmod/Core
module use $INSTALL_PATH/lmod/all
module load easybuild

export EASYBUILD_PREFIX=/srv/software/el8/ppc64le/eb/build
export XDG_CONFIG_HOME=$EASYBUILD_PREFIX/config  # "home" config files
export EASYBUILD_CONFIGFILES=$EASYBUILD_PREFIX/easyconfigs-fnal-hpc/ebconfig/config_wc_ppc64le.cfg
#export XDG_CONFIG_DIRS=  # other config files
export EASYBUILD_BUILDPATH=/tmp/simone/easybuild_ppc64le/build
export EASYBUILD_SOURCEPATH=/tmp/simone/easybuild_ppc64le/sources
export EASYBUILD_CONTAINERPATH=/tmp/simone/easybuild_ppc64le/containers
export EASYBUILD_REPOSITORYPATH=/tmp/simone/easybuild_ppc64le/ebfiles_repo
export EASYBUILD_INSTALLPATH_SOFTWARE=$INSTALL_PATH
export EASYBUILD_INSTALLPATH_MODULES=$INSTALL_PATH/lmod
export EASYBUILD_ROBOT_PATHS=$EASYBUILD_PREFIX/easyconfigs-fnal-hpc/wc/el8_ppc64le
export EASYBUILD_EXTERNAL_MODULES_METADATA=$EASYBUILD_PREFIX/easyconfigs-fnal-hpc/wc/el8_ppc64le/*.cfg
export EASYBUILD_INCLUDE_MODULE_NAMING_SCHEMES=$EASYBUILD_PREFIX/easyconfigs-fnal-hpc/lmod/LowerFlatMNS.py

