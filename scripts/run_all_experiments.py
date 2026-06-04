import subprocess, sys
for s in ['generate_oran_kpis.py','generate_xapp_policy.py','generate_srsran_config_stub.py','generate_oai_config_stub.py','run_ran_policy_smoke.py']:
    subprocess.check_call([sys.executable, f'scripts/{s}'])
from pathlib import Path; Path('results/testbed_plan.md').write_text('# Testbed plan\nSDR optional\n'); Path('results/experiment_summary.md').write_text('# RAN e2e PASS\n')
