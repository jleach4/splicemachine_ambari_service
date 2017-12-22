# splicemachine_ambari_service




curl -u raj_ops:raj_ops -X POST -H 'X-Requested-By:ambari' -d'{"RequestInfo":{"context":"Execute an action", "action" : "install_splice_machine", "service_name" : "", "component_name":"", "hosts":"127.0.0.1"}}' http://127.0.0.1:8080/api/v1/clusters/Sandbox/requests




curl -u <username>:<password> -X POST -H 'X-Requested-By:ambari' -d'{"RequestInfo":{"context":"Execute an action", "action" : "install_kerberos_package", "service_name" : "", "component_name":"", "hosts":"<comma-separated-hosts>"}}' http://<ambari-host>:<ambari-port>/api/v1/clusters/<cluster-name>/requests