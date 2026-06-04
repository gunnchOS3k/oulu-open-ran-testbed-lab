from pathlib import Path; import json; from oulu_ran.srsran_config import srsran_stub; Path('configs/srsran/stub.json').write_text(json.dumps(srsran_stub()))
