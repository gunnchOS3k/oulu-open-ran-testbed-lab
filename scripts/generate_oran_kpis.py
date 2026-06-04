from pathlib import Path
import yaml
p=Path('results/oran_kpi_schema.yaml'); p.parent.mkdir(exist_ok=True); p.write_text(yaml.dump({'kpis':['latency_ms','prb_util']}))
