import os
from pathlib import Path
import json

file_path = Path(os.path.realpath(__file__))

# source of nodes list: https://nodes.fediverse.party/nodes.json
with open(file_path.parent.parent.joinpath("data").joinpath("fediverse_nodes.json")) as f:
    sites = json.loads(f.read())

def rule(site):
    s = """Rule {{
    Matches {{
        Site("{0}")
    }}
}};""".format(
        site
    )

    return s


optic = """DiscardNonMatching;

"""

optic += (
        "// source of fediverse sites: https://nodes.fediverse.party/nodes.json\n"
)
optic += "\n\n".join([rule(site) for site in sites])

print(optic)
