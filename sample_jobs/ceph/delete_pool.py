import json
import uuid

import etcd

job_id1 = str(uuid.uuid4())

job = {
    "integration_id": "ab3b125e-4769-4071-a349-e82b380c11f4",
    "run": "ceph.objects.Pool.flows.DeletePool",
    "status": "new",
    "parameters": {
        "Pool.pool_id": 3,
        "Pool.poolname": "testEcPool1",
    },
    "type": "sds",
    "node_ids": ["c8b88d30-e714-471e-880a-0514216d80c1"]
}

print("/queue/%s/" % job_id1)
client = etcd.Client(host="10.70.43.135", port=2379)
client.write("/queue/%s" % job_id1, None, dir=True)
client.write("/queue/%s/payload" % job_id1, json.dumps(job))
client.write("/queue/%s/status" % job_id1, "new")

