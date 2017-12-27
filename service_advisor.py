#!/usr/bin/env ambari-python-wrap
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import imp
import math
import os
import re
import socket
import traceback

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STACKS_DIR = os.path.join(SCRIPT_DIR, '../../../stacks/')
PARENT_FILE = os.path.join(STACKS_DIR, 'service_advisor.py')

try:
  with open(PARENT_FILE, 'rb') as fp:
    service_advisor = imp.load_module('service_advisor', fp, PARENT_FILE, ('.py', 'rb', imp.PY_SOURCE))
except Exception as e:
  traceback.print_exc()
  print "Failed to load parent"

class SpliceMachineServiceAdvisor(service_advisor.ServiceAdvisor):

  def __init__(self, *args, **kwargs):
    self.as_super = super(SpliceMachineServiceAdvisor, self)
    self.as_super.__init__(*args, **kwargs)

  def colocateService(self, hostsComponentsMap, serviceComponents):

  def getServiceConfigurationRecommendations(self, configurations, clusterData, services, hosts):

    # Update HDFS properties in core-site
    if "core-site" in services["configurations"]:
      core_site = services["configurations"]["core-site"]["properties"]
      putCoreSiteProperty = self.putProperty(configurations, "core-site", services)

      for property, desired_value in self.getCoreSiteDesiredValues().iteritems():
        if property not in core_site or core_site[property] != desired_value:
          putCoreSiteProperty(property, desired_value)

  def getServiceConfigurationsValidationItems(self, configurations, recommendedDefaults, services, hosts):

    # validate recommended properties in core-site
    siteName = "core-site"
    method = self.validateCoreSiteConfigurations
    items = self.validateConfigurationsForSite(configurations, recommendedDefaults, services, hosts, siteName, method)
 #   items.extend(resultItems)

    return items


  def validateCoreSiteConfigurations(self, properties, recommendedDefaults, configurations, services, hosts):
    core_site = properties
    validationItems = []
    for property, desired_value in self.getCoreSiteDesiredValues().iteritems():
      if property not in core_site or core_site[property] != desired_value:
        message = "Splice Machine requires this property to be set to the recommended value of " + desired_value
        validationItems.append({"config-name": property, "item": self.getWarnItem(message)})
    return self.toConfigurationValidationProblems(validationItems, "core-site")

    def getCoreSiteDesiredValues(self):
        core_site_desired_values = {
            "ipc.server.listen.queue.size" : "3300"
        }
    return core_site_desired_values

    def getHDFSSiteDesiredValues(self):
        hdfs_site_desired_values = {
            "dfs.datanode.handler.count" : "20"
        }
    return core_site_desired_values

    def getHBaseSiteDesiredValues(self):
        hbase_site_desired_values = {
            "hbase.regionserver.global.memstore.size" : "0.25",
            "hfile.block.cache.size" : "0.25",
            "hbase.regionserver.handler.count" : "200",
            "hbase.client.scanner.caching" : "1000",
            "hbase.hstore.blockingStoreFiles" : "20",
            "hbase.hstore.compactionThreshold" : "5"
        }
    return hbase_site_desired_values
