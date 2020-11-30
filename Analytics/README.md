# Oracle Analytics Cloud

This page contains sample scripts to Start, Stop and Scale Analytics Cloud instances using OCI Python SDK

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
  
## Authenticate with Analytics Client 

The below code piece will load the `config` from the default directory and authenticates with OCI using the `oci.analytics.AnalyticsClient` class

  ```
  import oci
  config = oci.config.from_file()
  oac = oci.analytics.AnalyticsClient(config)
  ```

## Scale Up using Freeform Tags

Add a freeform tag `max_ocpu` to the Analytics instance with value as the number of OCPU needed after scaling. Using this value we will scale the Analytics instance using below code.

  ```
  import oci
  config = oci.config.from_file()
  oac = oci.analytics.AnalyticsClient(config)
  oac_ocid = '<OAC_INSTANCE_OCID>'
  oac_ins = oac.get_analytics_instance(oac_ocid).data
  max_ocpu = int(oac_ins.freeform_tags['max_ocpu'])
  # Scale up using Freeform tag max_ocpu
  oac.scale_analytics_instance(oac_ocid,oci.analytics.models.ScaleAnalyticsInstanceDetails(capacity=oci.analytics.models.Capacity(capacity_type="OLPU_COUNT",capacity_value=max_ocpu)))
  ```
 
