import oci
config = oci.config.from_file()
# Analytics Instance
oac_ocid = '<OAC_INSTANCE_OCID>'
oac = oci.analytics.AnalyticsClient(config)
oac_ins = oac.get_analytics_instance(oac_ocid).data
# Edit below if you don't have freeform tags 
max_ocpu = int(oac_ins.freeform_tags['max_ocpu'])
# Scale up using Freeform tag max_ocpu
oac.scale_analytics_instance(oac_ocid,oci.analytics.models.ScaleAnalyticsInstanceDetails(capacity=oci.analytics.models.Capacity(capacity_type="OLPU_COUNT",capacity_value=max_ocpu)))
