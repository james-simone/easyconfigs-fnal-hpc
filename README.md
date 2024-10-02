# easyconfigs-fnal-hpc
A collection of [EasyBuild](https://easybuild.io/) config files for installing software toolchains on HPC clusters.

## Installation procedure

There are a handfull of software pacakges such as CMake, git, and CUDA installed manually and not with EasyBuild. They are referenced as "external" modules in the EasyConfig files. These packages could just as easily be installed with EasyBuild.

1. Bootstap an installation of EasyBuild into the software installation directory. This involves a three-stage process described in this [video](https://mdc-easybuild.readthedocs.io/en/latest/demos/bootstrapping.html#demo-bootstrapping) as well as the EasyBuild tutorials.
2. Clone this repository on your build system.
3. Source the EasyBuild configuration script in ./setup specific to the target system, e.g., ./setup/setup_lq.sh.
4.  The EasyConfigs for each system are in separate directories named after the system on the enterprise Linux major version, e.g., ./lq/el8/ .


