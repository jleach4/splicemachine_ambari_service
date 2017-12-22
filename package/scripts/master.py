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

Splice Machine

"""

import glob
import grp
import os
import pwd
import sys

from resource_management import *

reload(sys)
sys.setdefaultencoding('utf8')


class Master(Script):
    def install(self, env):
        import params
        env.set_params(params)

    #debug info

    Execute('echo cloned scripts dir is: ' + params.scripts_dir)

    Execute('echo list of config dump: ' + str(', '.join(params.list_of_configs)))
    Execute('echo master config dump: ' + str(', '.join(params.master_configs)))

    Execute('echo ambari host: ' + params.ambari_server_host)
    Execute('echo namenode host: ' + params.namenode_host)
    Execute('echo nimbus host: ' + params.nimbus_host)
    Execute('echo hive metastore host: ' + params.hive_metastore_host)
    Execute('echo supervisor hosts: ' + params.supervisor_hosts)
    Execute('echo hbase zookeeper: ' + params.hbase_zookeeper)
    Execute('echo kafka host: ' + params.kafka_broker_host)
    Execute('echo activemq host: ' + params.activemq_host)

    #Execute('echo kafka-broker dump: ' + str(', '.join(params.config['configurations']['kafka-broker'])))
    Execute('echo demo port: ' + params.port)
    Execute('echo ambari port: ' + params.ambari_port)
    Execute('echo namenode port: ' + params.namenode_port)
    Execute('echo hive MS port: ' + params.hive_metastore_port)
    Execute('echo kafka port: ' + params.kafka_port)
    #Execute('echo stack_version: ' + params.stack_version_unformatted)

if __name__ == "__main__":
    Master().execute()