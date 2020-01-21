# OCI
This script will stop Compute, Autonomous Databases and OAC OCI Native instances (Tokyo only) from all the compartments.

Edit the below values as per your tenancy

```
# Tenancy & User details for Authentication ( Change as needed)
compartment_id = 'ocid1.tenancy.oc1..xxxxxxxxxxxxxxxxxxx' # Tenancy & Root compartment OCID
userocid = '' # User OCID 
home_region = 'us-ashburn-1' # Home Region
key_file = '/~path/oci_api_key.pem' # Prvate file for User Authentication
fingerprint = '' # Finger print of the public key added in user tokens
```

