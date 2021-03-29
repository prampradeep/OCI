# OCI Compute

This page contains sample scripts to Start, Stop OCI Cloud instances using OCI Python SDK

## Pre-requisites

- Make sure you have python installed, preferably python3.6 and above 
- Install oci, oci-cli package 

  ```
  pip3 install oci oci-cli
  ```
- OCI Config file in **$HOME/.oci/config**, Sample format below 

  ```
  [DEFAULT]
  user = <USER_OCID>
  fingerprint = <FINGERPRINT>
  key_file = <PATH_TO_PRIVATE_KEY>
  tenancy = <TENANCY_OCID>
  region = <REGION>
  ```
  
## Authenticate with Compute Client 

The below code piece will load the `config` from the default directory and authenticates with OCI using the `oci.core.ComputeClient` class

  ```
  import oci
  config = oci.config.from_file()
  oac = oci.core.ComputeClient(config)
  ```
