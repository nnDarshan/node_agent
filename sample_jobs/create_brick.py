import etcd
#from tendrl.commons.objects.job import Job
import json
import uuid


integration_id = "ab3b125e-4769-4071-a349-e82b380c11f4"
job_id = str(uuid.uuid4())

payload = {
    "integration_id": integration_id,
    "run": "tendrl.gluster.flows.CreateGlusterBrick",
    "parameters": {
        "GlusterBrick.brick_dict": {
            "10.70.43.11:/mnt/darshan_Multinode1/b101": {
                "node_id": "07d57922-dadf-49f0-8b1a-c54ffadd4b85",
                "disk": "vdh"
            },
            "10.70.43.11:/mnt/darshan_Multinode2/b102": {
                "node_id": "07d57922-dadf-49f0-8b1a-c54ffadd4b85",
                "disk": "vdi"
            },
            "10.70.42.202:/mnt/darshan_Multinode3/b103": {
                "node_id": "vdd",
                "disk": "2d6626a4-fbe3-4785-8b95-ba329d469d99"
            },
            "10.70.42.202:/mnt/darshan_Multinode4/b104": {
                "node_id": "2d6626a4-fbe3-4785-8b95-ba329d469d99",
                "disk": "vde"
            },
        }
    },
    "type": "sds",
    "node_ids": ["07d57922-dadf-49f0-8b1a-c54ffadd4b85"]
}

def run():
    client = etcd.Client(host="10.70.43.135", port=2379)
    client.write("/queue/%s/payload" % job_id, json.dumps(payload))
    client.write("/queue/%s/status" % job_id, "new")
    client.write("/queue/%s/job_id" % job_id, job_id)
    print job_id

if __name__ == "__main__":
    run()
