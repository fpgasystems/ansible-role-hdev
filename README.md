hdev
=========

Ansible role to install and configure [hdev](https://github.com/fpgasystems/hdev).

Requirements
------------

Hdev can be installed fully using this role. However for some functionality of hdev other tools need to be installed. The following tools/libraries are used by hdev, but are not provided by this role and should be installed separately:
- vivado
- vitis
- xbutil
- ami_tool

Role Variables
--------------

> [!NOTE]
> this interface is an early draft and bound to change. Expect breaking changes

```yaml
hdev_version: main
```
Selects the version of hdev to be installed. This can be a branch name, commit id or tag.

---

This role expects to be provided with two dictionaries that manage the main configuration of hdev.

### Constants
The first dictionary, `hdev_constants` defines the hdev constants. These are defined in `defaults/main.yml` and all have been provided with sensible defaults. The main ones that need to be changed for a specific cluster configuration are:
- `ACAP_SERVERS_LIST`
- `ASOC_SERVERS_LIST`
- `BUILD_SERVERS_LIST`
- `FPGA_SERVERS_LIST`
- `GPU_SERVERS_LIST`
- `NIC_SERVERS_LIST`

Provide an enter-separated list with the servernames that belong to each category.

### Servers
The second dictionary, `hdev_servers` defines the servers that are defined in the `devices/` directory of hdev.
This dictionary is by default empty and should be entirely provided by the user of the role.

The dictionary is structured as follows:
```yaml
hdev_servers:
  server_name:
    device_category:
    device_category:
    ...
  server_name:
    device_category:
    device_category:
    ...
```
The `server_name` is the hostname of the server it describes. The `device_category` can be one of three device categories: `network`, `acap_fpga` and `gpu`. Each category has one or more device indeces that are indicated by an object starting from `1:`. Each device index has a set of attributes that are specific to the device category.

The network device category
```yaml
network:
  1:
    bdf: String
    device_type: String
    device_name: String
    ip: [ String, ... ]
    mac: [ String, ... ]
  2:
    ...
```

The FPGA/ACAP/ASOC device category
```yaml
acap_fpga:
  1:
    bdf_root: String
    bdf_upstream: String
    device_name: String
    device_type: String
    ip: [ String, ... ]
    linkctl: Int
    mac: [ String, ... ]
    platform: String
    serial_number: String
  2:
    ...
```

The GPU device category
```yaml
gpu:
  1:
    bus: String
    device_type: String
    gpu_id: String
    serial_number: String
    unique_id: String
  2:
    ...
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

TODO: when the `amd_apm` role is done and published on Galaxy, a link should be given here.

Example Playbook
----------------

This is an example playbook for a four machine cluster.

- alveo-build-01 is a build server with no devices inside.
- alveo-u55c-01 is a server with an AMD Alveo U55c FPGA.
- alveo-u55c-02 is another FPGA server with the same FPGA.
- alveo-box-01 is a server with two GPUs, an Alveo U55c FPGA and a Versal VCK5000 ACAP.

Each machine also has a high speed network interface card.

```yaml
    - hosts: servers
      vars_files:
        - vars/hdev.yml
      roles:
        - role: hdev
```
Inside `vars/hdev.yml`

```yaml
hdev_constants:
  BUILD_SERVERS_LIST: |
    alveo-build-01.cluster.example.com
  FPGA_SERVERS_LIST: |
    alveo-u55c-01.cluster.example.com
    alveo-u55c-02.cluster.example.com
    alveo-box-01.cluster.example.com
  GPU_SERVERS_LIST: |
    alveo-box-01.cluster.example.com
  ACAP_SERVERS_LIST: |
    alveo-box-01.cluster.example.com
  NIC_SERVERS_LIST: |
    alveo-build-01.cluster.example.com
    alveo-u55c-01.cluster.example.com
    alveo-u55c-02.cluster.example.com
    alveo-box-01.cluster.example.com
  XILINXD_LICENSE_FILE: |
    1000@xilinx-license-server.example.com
    1001@xilinx-license-server.example.com

hdev_servers:
  alveo-build-01.cluster.example.com:
    network:
      1:
        bdf: "00:00.0"
        device_type: "nic"
        device_name: "MT27800"
        ip:
          - "XXX.XXX.XXX.XXX"
          - "XXX.XXX.XXX.XXX"
        mac:
          - "XX:XX:XX:XX:XX:XX"
          - "XX:XX:XX:XX:XX:XX"

  alveo-u55c-01.cluster.example.com:
    network:
      1:
        bdf: "00:00.0"
        device_type: "nic"
        device_name: "MT27800"
        ip:
          - "XXX.XXX.XXX.XXX"
          - "XXX.XXX.XXX.XXX"
        mac:
          - "XX:XX:XX:XX:XX:XX"
          - "XX:XX:XX:XX:XX:XX"
    acap_fpga:
      1:
        bdf_root: "00:00.0"
        bdf_upstream: "00:00.0"
        device_name: "xcu280_u55c_0"
        device_type: "fpga"
        ip:
          - "XXX.XXX.XXX.XXX"
          - "XXX.XXX.XXX.XXX"
        linkctl: 58
        mac:
          - "XX:XX:XX:XX:XX:XX"
          - "XX:XX:XX:XX:XX:XX"
        platform: "xilinx_u55c_gen3x16_xdma_3_202210_1"
        serial_number: "0000000000000"

  alveo-u55c-02.cluster.example.com:
    network:
      1:
        bdf: "00:00.0"
        device_type: "nic"
        device_name: "MT27800"
        ip:
          - "XXX.XXX.XXX.XXX"
          - "XXX.XXX.XXX.XXX"
        mac:
          - "XX:XX:XX:XX:XX:XX"
          - "XX:XX:XX:XX:XX:XX"
    acap_fpga:
      1:
        bdf_root: "00:00.0"
        bdf_upstream: "00:00.0"
        device_name: "xcu280_u55c_0"
        device_type: "fpga"
        ip:
          - "XXX.XXX.XXX.XXX"
          - "XXX.XXX.XXX.XXX"
        linkctl: 58
        mac:
          - "XX:XX:XX:XX:XX:XX"
          - "XX:XX:XX:XX:XX:XX"
        platform: "xilinx_u55c_gen3x16_xdma_3_202210_1"
        serial_number: "0000000000000"

  alveo-box-01.cluster.example.com:
    network:
      1:
        bdf: "00:00.0"
        device_type: "nic"
        device_name: "MT27800"
        ip:
          - "XXX.XXX.XXX.XXX"
          - "XXX.XXX.XXX.XXX"
        mac:
          - "XX:XX:XX:XX:XX:XX"
          - "XX:XX:XX:XX:XX:XX"
    acap_fpga:
      1:
        bdf_root: "00:00.0"
        bdf_upstream: "00:00.0"
        device_name: "xcu280_u55c_0"
        device_type: "fpga"
        ip:
          - "XXX.XXX.XXX.XXX"
          - "XXX.XXX.XXX.XXX"
        linkctl: 58
        mac:
          - "XX:XX:XX:XX:XX:XX"
          - "XX:XX:XX:XX:XX:XX"
        platform: "xilinx_u55c_gen3x16_xdma_3_202210_1"
        serial_number: "0000000000000"
      2:
        bdf_root: "00:00.0"
        bdf_upstream: "00:00.0"
        device_name: "xcvc1902_1"
        device_type: "acap"
        ip:
          - "XXX.XXX.XXX.XXX"
          - "XXX.XXX.XXX.XXX"
        linkctl: 58
        mac:
          - "XX:XX:XX:XX:XX:XX"
          - "XX:XX:XX:XX:XX:XX"
        platform: "xilinx_vck5000_gen4x8_qdma_2_202220_1"
        serial_number: "0000000000000"

    gpu:
      1:
        bus: "00:00.0"
        device_type: "gpu"
        gpu_id: "0x740f"
        serial_number: "000000000000"
        unique_id: "0x00000000000000"
      2:
        bus: "00:00.0"
        device_type: "gpu"
        gpu_id: "0x740f"
        serial_number: "000000000000"
        unique_id: "0x00000000000000"

```

License
-------

MIT

Author Information
------------------

This role was created in 2025 by [Geert Roks](https://github.com/GeertRoks), maintainer for the Heterogeneous Accelerated Compute Cluster (HACC) at the ETH Zürich, Systems Group.
