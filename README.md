ansible-role-hdev
=========

Ansible role to install and configure [hdev](https://github.com/fpgasystems/hdev).

Installation
------------

Add this role as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to the `roles/` directory of your Ansible project.

```bash
cd <path/to/your/ansible/project>
mkdir -p roles/
git submodule add https://github.com/fpgasystems/ansible-role-hdev roles/hdev
```

This assumes you store your Ansible project in a git repo itself. If this is not the case, then just use `git clone`.

Requirements
------------

Hdev can be installed fully using this role. However for some functionality of hdev other tools need to be installed. The following tools/libraries are used by hdev, but are not provided by this role and should be installed separately:
- vivado
- vitis
- xbutil
- ami_tool

Role Variables
--------------

```yaml
hdev_version: "main"
```
Selects the version of hdev to be installed. This can be a branch name, commit id or tag.

```yaml
hdev_constants_dir: ""
```
Local directory that contains the constants that need to be loaded on the target. Check the hdev documentation for the available constants.

```yaml
hdev_cmdb_dir: ""
```
Local directory that contains the cmdb that need to be loaded on the target. Check the hdev documentation for how to structure the cmdb.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

TODO: when the `amd_fpga_toolchain`, `amd_XRT_flow` and `amd_AVED_flow` roles are done and published, a link should be given here.

Example Playbook
----------------

An example playbook for the following folder structure:

```
.
├── example-playbook.yml
├── roles/
│   └── hdev/
│       └── <this role>
└── files/
    └── hdev/
        ├── constants/
        │   ├── ACAP_SERVERS_LIST
        │   ├── AMI_HOME
        │   ├── ASOC_SERVERS_LIST
        │   └── < etc... >
        └── cmdb/
            ├── node-01.example.com/
            │   ├── devices_acap_fpga
            │   ├── devices_gpu
            │   └── devices_network
            ├── node-02.example.com/
            │   ├── devices_acap_fpga
            │   └── devices_network
            └── < etc... >
```

Inside the `example-playbook.yml`
```yaml
    - hosts: servers

      roles:
        - role: hdev
          vars:
            hdev_version: "2025.5.5"
            hdev_constants_dir: "./files/hdev/constants"
            hdev_cmdb_dir: "./files/hdev/cmdb"
```

License
-------

MIT

Author Information
------------------

This role was created in 2025 by [Geert Roks](https://github.com/GeertRoks), maintainer for the Heterogeneous Accelerated Compute Cluster (HACC) at the ETH Zürich, Systems Group.
