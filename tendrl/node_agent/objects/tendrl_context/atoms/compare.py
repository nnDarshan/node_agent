import etcd
from tendrl.node_agent.config import TendrlConfig

config = TendrlConfig()


class Compare(object):
    def run(self, parameters):
        sds_name = parameters.get("Tendrl_context.sds_name")
        sds_version = parameters.get("Tendrl_context.sds_version")
        etcd_kwargs = {'port': int(config.get("common", "etcd_port")),
                       'host': config.get("common", "etcd_connection")}

        client = etcd.Client(**etcd_kwargs)
        # get the node_agent_key some how
        # for now reading it from the json file

        with open("/etc/tendrl/node_agent/node_context") as f:
            node_id = f.read()

        path = "/nodes/%s/Tendrl_context" % node_id
        try:
            tendrl_context = client.read(path)
        except etcd.EtcdKeyNotFound:
            return False
        etcd_sds_name = ""
        etcd_sds_version = ""
        for el in tendrl_context.children:
            if el.key.split('/')[-1] == "sds_name":
                etcd_sds_name = el.value
            if el.key.split('/')[-1] == "sds_version":
                etcd_sds_version = el.value
        if etcd_sds_version == sds_version and etcd_sds_name == sds_name:
            return True
        else:
            return False
