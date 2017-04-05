import json
import uuid

import etcd

job_id1 = str(uuid.uuid4())

job = {
    "integration_id": "ab3b125e-4769-4071-a349-e82b380c11f4",
    "run": "tendrl.flows.ImportCluster",
    "status": "new",
    "parameters": {
        "TendrlContext.integration_id": "ab3b125e-4769-4071-a349-e82b380c11f4",
        "Node[]": ["2d6626a4-fbe3-4785-8b95-ba329d469d99","07d57922-dadf-49f0-8b1a-c54ffadd4b85"],
        "DetectedCluster.sds_pkg_name": "gluster"
    },
    "type": "node",
    "node_ids": ["2d6626a4-fbe3-4785-8b95-ba329d469d99","07d57922-dadf-49f0-8b1a-c54ffadd4b85"],
}

print("/queue/%s/" % job_id1)
client = etcd.Client(host="10.70.43.135", port=2379)
client.write("/queue/%s" % job_id1, None, dir=True)
client.write("/queue/%s/payload" % job_id1, json.dumps(job))
client.write("/queue/%s/status" % job_id1, "new")
