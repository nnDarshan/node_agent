import json
import uuid

import etcd

job_id1 = str(uuid.uuid4())

job = {
    "integration_id": "ab3b125e-4769-4071-a349-e82b380c11f4",
    "run": "ceph.objects.Rbd.flows.ResizeRbd",
    "status": "new",
    "parameters": {
        "Rbd.pool_id": 4,
        "Rbd.name": "mmrbd2",
        "Rbd.size": 2048
    },
    "type": "sds",
    "node_ids": ["434d39ba-fff7-4b22-9ea0-c0fba75c27da"]
}

print("/queue/%s/" % job_id1)
client = etcd.Client(host="host", port=2379)
client.write("/queue/%s" % job_id1, None, dir=True)
client.write("/queue/%s/payload" % job_id1, json.dumps(job))
client.write("/queue/%s/status" % job_id1, "new")
