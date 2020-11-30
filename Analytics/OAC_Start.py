import oci
config = oci.config.from_file()
# Analytics Instance
oac_ocid = '<OAC_INSTANCE_OCID>'
oac = oci.analytics.AnalyticsClient(config)
oac_ins = oac.get_analytics_instance(oac_ocid).data
# Verify Instance state and execute START if INACTIVE
if oac_ins.lifecycle_state == "INACTIVE":
    oac.start_analytics_instance(oac_ocid)
    print("Instance START command initiated")
else:
    print("Instance is AVAILABLE")
