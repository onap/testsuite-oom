# File generated from /opt/config
#
GLOBAL_INJECTED_AAI1_IP_ADDR = "aai-service.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_AAI2_IP_ADDR = "N/A"
GLOBAL_INJECTED_APPC_IP_ADDR = "appc-sdnhost.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_ARTIFACTS_VERSION = "1.1.0-SNAPSHOT"
GLOBAL_INJECTED_CLAMP_IP_ADDR = "clamp.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_CLOUD_ENV = "openstack"
GLOBAL_INJECTED_DCAE_IP_ADDR = "dcae-controller.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_DNS_IP_ADDR = "10.0.100.1"
GLOBAL_INJECTED_DOCKER_VERSION = "1.1-STAGING-latest"
#GLOBAL_INJECTED_EXTERNAL_DNS = "N/A"
GLOBAL_INJECTED_GERRIT_BRANCH = "master"
GLOBAL_INJECTED_KEYSTONE = "{{ .Values.openStackKeyStoneUrl }}"
GLOBAL_INJECTED_MR_IP_ADDR = "dmaap.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_MSO_IP_ADDR = "mso.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_NETWORK = "{{ .Values.openStackPrivateNetId }}"
GLOBAL_INJECTED_NEXUS_DOCKER_REPO = "nexus3.onap.org:10001"
GLOBAL_INJECTED_NEXUS_PASSWORD = "docker"
GLOBAL_INJECTED_NEXUS_REPO = "https://nexus.onap.org/content/sites/raw"
GLOBAL_INJECTED_NEXUS_USERNAME = "docker"
GLOBAL_INJECTED_OPENO_IP_ADDR = "msb-iag.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_OPENSTACK_PASSWORD = "{{ .Values.openStackEncryptedPassword }}"
GLOBAL_INJECTED_OPENSTACK_TENANT_ID = "{{ .Values.openStackTenantId }}"
GLOBAL_INJECTED_OPENSTACK_USERNAME = "{{ .Values.openStackUserName }}"
GLOBAL_INJECTED_POLICY_IP_ADDR = "pypdp.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_POLICY_HEALTHCHECK_IP_ADDR = "drools.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_PORTAL_IP_ADDR = "portalapps.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_REGION = "{{ .Values.openStackRegion }}"
GLOBAL_INJECTED_REMOTE_REPO = "http://gerrit.onap.org/r/testsuite/properties.git"
GLOBAL_INJECTED_SDC_IP_ADDR = "sdc-be.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_SDC_FE_IP_ADDR = "sdc-fe.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_SDC_BE_IP_ADDR = "sdc-be.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_SDNC_IP_ADDR = "sdnhost.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_SDNC_PORTAL_IP_ADDR = "sdnc-portal.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_SO_IP_ADDR = "mso.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_VID_IP_ADDR = "vid-server.{{ .Values.nsPrefix }}"
GLOBAL_INJECTED_VM_FLAVOR = "{{ .Values.openStackFlavourMedium }}"
GLOBAL_INJECTED_VM_IMAGE_NAME = "{{ .Values.ubuntuImage }}"
GLOBAL_INJECTED_PUBLIC_NET_ID = "{{ .Values.openStackPublicNetId }}"
GLOBAL_INJECTED_PROPERTIES = {
    "GLOBAL_INJECTED_AAI1_IP_ADDR" : "aai-service.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_APPC_IP_ADDR" : "appc-sdnhost.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_ARTIFACTS_VERSION" : "1.1.0-SNAPSHOT",
    "GLOBAL_INJECTED_CLAMP_IP_ADDR" : "clamp.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_CLOUD_ENV" : "openstack",
    "GLOBAL_INJECTED_DCAE_IP_ADDR" : "dcae-controller.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_DNS_IP_ADDR" : "10.0.100.1",
    "GLOBAL_INJECTED_DOCKER_VERSION" : "1.1-STAGING-latest",
    "GLOBAL_INJECTED_GERRIT_BRANCH" : "master",
    "GLOBAL_INJECTED_KEYSTONE" : "{{ .Values.openStackKeyStoneUrl }}",
    "GLOBAL_INJECTED_MR_IP_ADDR" : "dmaap.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_MSO_IP_ADDR" : "mso.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_NETWORK" : "{{ .Values.openStackPrivateNetId }}",
    "GLOBAL_INJECTED_NEXUS_DOCKER_REPO" : "nexus3.onap.org:10001",
    "GLOBAL_INJECTED_NEXUS_PASSWORD" : "docker",
    "GLOBAL_INJECTED_NEXUS_REPO" : "https://nexus.onap.org/content/sites/raw",
    "GLOBAL_INJECTED_NEXUS_USERNAME" : "docker",
    "GLOBAL_INJECTED_OPENO_IP_ADDR" : "msb-iag.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_OPENSTACK_PASSWORD" : "{{ .Values.openStackEncryptedPassword }}",
    "GLOBAL_INJECTED_OPENSTACK_TENANT_ID" : "{{ .Values.openStackTenantId }}",
    "GLOBAL_INJECTED_OPENSTACK_USERNAME" : "{{ .Values.openStackUserName }}",
    "GLOBAL_INJECTED_POLICY_IP_ADDR" : "pypdp.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_POLICY_HEALTHCHECK_IP_ADDR" : "drools.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_PORTAL_IP_ADDR" : "portalapps.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_REGION" : "{{ .Values.openStackRegion }}",
    "GLOBAL_INJECTED_REMOTE_REPO" : "http://gerrit.onap.org/r/testsuite/properties.git",
    "GLOBAL_INJECTED_SDC_FE_IP_ADDR" : "sdc-fe.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_SDC_BE_IP_ADDR" : "sdc-be.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_SDNC_IP_ADDR" : "sdnhost.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_SDNC_PORTAL_IP_ADDR" : "sdnc-portal.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_SO_IP_ADDR" : "mso.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_VID_IP_ADDR" : "vid-server.{{ .Values.nsPrefix }}",
    "GLOBAL_INJECTED_VM_FLAVOR" : "{{ .Values.openStackFlavourMedium }}",
    "GLOBAL_INJECTED_VM_IMAGE_NAME" : "{{ .Values.ubuntuImage }}",
    "GLOBAL_INJECTED_PUBLIC_NET_ID" : "{{ .Values.openStackPublicNetId }}"
}
