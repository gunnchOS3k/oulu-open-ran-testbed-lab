from pathlib import Path; import json; from oulu_ran.oai_config import oai_stub; Path('configs/oai/stub.json').write_text(json.dumps(oai_stub()))
