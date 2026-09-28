import sys
import json
from client import SweepAndPrune

sap = SweepAndPrune()

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "sweep_and_prune",
                        "description": "Perform broadphase Sweep-and-Prune collision detection on list of AABBs",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "boxes": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "string"},
                                            "min_x": {"type": "number"},
                                            "max_x": {"type": "number"},
                                            "min_y": {"type": "number"},
                                            "max_y": {"type": "number"}
                                        },
                                        "required": ["id", "min_x", "max_x", "min_y", "max_y"]
                                    }
                                }
                            },
                            "required": ["boxes"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "sweep_and_prune":
            boxes = [SweepAndPrune.AABB(b["id"], b["min_x"], b["max_x"], b["min_y"], b["max_y"]) for b in args["boxes"]]
            pairs = sap.find_potential_collisions(boxes)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"potential_pairs": pairs})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
