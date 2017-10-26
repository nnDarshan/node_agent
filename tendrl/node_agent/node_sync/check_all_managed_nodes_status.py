import etcd

from tendrl.commons.objects.job import Job
import uuid


def update_brick_status(fqdn, integration_id):
    _job_id = str(uuid.uuid4())
    _params = {
        "TendrlContext.integration_id": integration_id,
        "Node.fqdn": fqdn
    }
    _job_payload = {
        "tags": [
            "tendrl/integration/{0}".format(
                integration_id
            )
        ],
        "run": "gluster.flows.UpdateBrickStatus",
        "status": "new",
        "parameters": _params,
        "type": "sds"
    }
    Job(
        job_id=_job_id,
        status="new",
        payload=_job_payload
    ).save()


def run():
    try:
        nodes = NS._int.client.read("/nodes")
    except etcd.EtcdKeyNotFound:
        return

    for node in nodes.leaves:
        node_id = node.key.split('/')[-1]
        try:
            NS._int.client.write(
                "/nodes/{0}/NodeContext/status".format(node_id),
                "DOWN",
                prevExist=False
            )
            fqdn = NS._int.client.read(
                "/nodes/{0}/NodeContext/fqdn".format(node_id)
            ).value
            integration_id = NS._int.client.read(
                "nodes/{0}/TendrlContext/integration_id".format(node_id)
            ).value
            update_brick_status(fqdn, integration_id)
        except etcd.EtcdAlreadyExist:
            pass
    return
