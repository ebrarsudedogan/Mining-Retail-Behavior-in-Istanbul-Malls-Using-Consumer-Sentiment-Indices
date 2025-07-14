#written to organize de repository

import shutil
from pathlib import Path
import os

base_dir = Path.cwd().parent
daily_dir = base_dir / "data_analysis_daily"
weekly_dir = base_dir / "data_analysis_weekly"
monthly_dir = base_dir / "data_analysis_monthly"

weekly_dir.mkdir(exist_ok=True)
monthly_dir.mkdir(exist_ok=True)

notebooks = list(daily_dir.glob("*.ipynb"))

for nb in notebooks:
    for target_dir in [weekly_dir, monthly_dir]:
        target_nb_path = target_dir / nb.name
        shutil.copy(nb, target_nb_path)
        print(f"📄 Kopyalandı: {target_nb_path.name} → {target_dir.name}")

        fig_folder_name = f"{nb.stem}_figures"
        fig_folder_path = target_dir / fig_folder_name
        fig_folder_path.mkdir(exist_ok=True)
        print(f"📁 Oluşturuldu: {fig_folder_name} → {target_dir.name}")
