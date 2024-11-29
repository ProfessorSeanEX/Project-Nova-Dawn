# Grace.py

def grace_init(metadata):
    if not isinstance(metadata, dict):
        return {"error": "GRACE command requires metadata as a dictionary"}
    return {"status": "Grace Node Initialized", "metadata": metadata}
