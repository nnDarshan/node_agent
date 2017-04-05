import json
import uuid

import etcd

job_id1 = str(uuid.uuid4())

job = {
    "integration_id": "89604c6b-2eff-4221-96b4-e41319240240",
    "run": "ceph.objects.Rbd.flows.ResizeRbd",
    "status": "new",
    "parameters": {
        "Rbd.pool_id": 2,
        "Rbd.name": "testrbd1234",
        "Rbd.size": 2048
    },
    "type": "sds",
    "node_ids": ["819e96d7-4e1f-4460-95f7-8ddfb5b79834"]
}

print("/queue/%s/" % job_id1)
client = etcd.Client(host="10.70.42.39", port=2379)
client.write("/queue/%s" % job_id1, None, dir=True)
client.write("/queue/%s/payload" % job_id1, json.dumps(job))
client.write("/queue/%s/status" % job_id1, "new")
