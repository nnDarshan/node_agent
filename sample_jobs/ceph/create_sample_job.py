import json
import uuid

import etcd

job_id1 = str(uuid.uuid4())

job = {
    "integration_id": "ab3b125e-4769-4071-a349-e82b380c11f4",
    "run": "ceph.flows.CreatePool",
    "status": "new",
    "parameters": {
        "Pool.poolname": 'testEcPool2',
        "Pool.pg_num": 30,
        "Pool.min_size": 1,
        "Pool.size": 2048,
        "Pool.type": "erasure",
        "Pool.erasure_code_profile": "k4m2",
    },
    "type": "sds",
    "node_ids": ["c8b88d30-e714-471e-880a-0514216d80c1"]
}

print("/queue/%s/" % job_id1)
client = etcd.Client(host="10.70.43.135", port=2379)
client.write("/queue/%s" % job_id1, None, dir=True)
client.write("/queue/%s/payload" % job_id1, json.dumps(job))
client.write("/queue/%s/status" % job_id1, "new")

#        "Pool.type": "erasure",
#        "Pool.erasure_code_profile": "k4m2",
