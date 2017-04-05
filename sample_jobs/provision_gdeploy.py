import json
import uuid

import etcd

job_id1 = str(uuid.uuid4())

job = {
    "integration_id": "ab3b125e-4769-4071-a349-e82b380c11f4",
    "run": "tendrl.flows.SetupGdeploy",
    "status": "new",
    "parameters": {
        "TendrlContext.integration_id": "ab3b125e-4769-4071-a349-e82b380c11f4",
        "Node[]": ["9ffe89f5-6d60-48af-b788-f418bc508001"],
        "DetectedCluster.sds_pkg_name": "gluster"
    },
    "type": "node",
    "node_ids": ["9ffe89f5-6d60-48af-b788-f418bc508001"]
}

print("/queue/%s/" % job_id1)
client = etcd.Client(host="10.70.43.135", port=2379)
client.write("/queue/%s" % job_id1, None, dir=True)
client.write("/queue/%s/payload" % job_id1, json.dumps(job))
client.write("/queue/%s/status" % job_id1, "new")
