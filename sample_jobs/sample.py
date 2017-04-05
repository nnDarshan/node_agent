import etcd
#from tendrl.commons.objects.job import Job
import json
import uuid


integration_id = "ab3b125e-4769-4071-a349-e82b380c11f4"
job_id = str(uuid.uuid4())

payload = {
    "integration_id": integration_id,
    "run": "tendrl.gluster.flows.CreateVolume",
    "parameters": {
        "Volume.volname": 'darshan_sample',
        "Volume.bricks": [
            [
                {"10.70.43.11":"/mnt/darshan_sample4/sampleBrick1"},
                {"10.70.43.11":"/mnt/darshan_sample5/sampleBrick2"}
            ]
        ],
        "Volume.replica_count": "2",
        "Volume.force": True,
    },
    "type": "sds",
    "node_ids": ["5eefcf00-e123-43d5-9cc9-bf75b1c9d207"]
}

def run():
    client = etcd.Client(host="10.70.43.135", port=2379)
    client.write("/queue/%s/payload" % job_id, json.dumps(payload))
    client.write("/queue/%s/status" % job_id, "new")
    client.write("/queue/%s/job_id" % job_id, job_id)
    print job_id

if __name__ == "__main__":
    run()
