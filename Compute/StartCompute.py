import oci
config = oci.config.from_file()
# List of Compute Instances
ins_ocid = ['<OCID>']
compute = oci.core.ComputeClient(config)
for i in range(0,len(ins_ocid)):
    print(ins_ocid[i])
    ins_details = compute.get_instance(ins_ocid[i]).data
    if ins_details.lifecycle_state == 'STOPPED':
        compute.instance_action(ins_details.id, "START")
        print("Start action initiated on Instance ",ins_details.display_name)
    else:
        print("Cannot initiate START action as the instance ",ins_details.display_name," state is ",ins_details.lifecycle_state)
