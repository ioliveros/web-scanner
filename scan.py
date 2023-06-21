import json

scanlist = {}
with open("scanlist.txt") as f:
    for line in f.read().split("\n"):
        _line = line.strip()
        if not _line: continue
        scan_key = _line.split("GET")[-1].strip().split("HTTP/1.0")[0].strip()
        if scanlist.get(scan_key, None):
            scanlist[scan_key] += 1
        else:
            scanlist[scan_key] = 0

print(json.dumps(scanlist, indent=4))
