"""
Script de descarga de datasets desde Roboflow Universe.
Requiere: pip install roboflow python-dotenv

USO:
    1. Crea una cuenta gratuita en https://app.roboflow.com/
    2. Ve a Settings > API Key y copia tu API key
    3. Añádela en el fichero .env (en la raíz del proyecto):
           ROBOFLOW_API_KEY=rf_xxxxxxxxxxxxxx
    4. Ejecuta: python scripts/download_datasets.py

Los datasets se guardan en data/raw/<marca>/
⚠️  El fichero .env está en .gitignore → la key NO se sube a GitHub.
"""

from roboflow import Roboflow
from dotenv import load_dotenv
import os

# Carga variables del fichero .env (raíz del proyecto)
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

# ─── CONFIGURACIÓN ────────────────────────────────────────────────────────────
API_KEY = os.getenv("ROBOFLOW_API_KEY", "")   # se lee desde .env, nunca en el código
OUTPUT_FORMAT = "yolov8"       # formato compatible con YOLOv8/Ultralytics
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")

# ─── DATASETS SELECCIONADOS ───────────────────────────────────────────────────
# Cada entrada: (workspace_slug, project_slug, version, carpeta_destino)
DATASETS = [
    # Nokia – 300 imágenes
    ("nikitas-workspace-1jw6b", "nokia-jfqln", 1, "nokia"),

    # Samsung – 606 imágenes  ⭐11
    ("holland", "samsung-le5e2", 1, "samsung"),

    # Apple/iPhone logo – 1090 imágenes  ⭐6
    ("melnyk-workspace", "apple-logo-smfdm", 1, "iphone"),

    # Xiaomi Logo A – 50 imágenes  ⭐2 + 1 modelo
    ("boe-gpvhd", "xiaomi-logo", 1, "xiaomi"),

    # Xiaomi Logo B – 50 imágenes (combinar con el anterior)
    # ("hand-joint", "xiaomi-logo-detection", 1, "xiaomi"),

    # MOTOROLA: no hay dataset público → crear manualmente
    # Ver docs/dataset_comparison_table.md → sección Motorola
]

# ─── DESCARGA ─────────────────────────────────────────────────────────────────
def download_all():
    rf = Roboflow(api_key=API_KEY)

    for workspace, project_slug, version_num, folder in DATASETS:
        dest = os.path.join(BASE_DIR, folder)
        os.makedirs(dest, exist_ok=True)

        print(f"\n{'='*60}")
        print(f"⬇️  Descargando: {project_slug} → data/raw/{folder}/")
        print(f"{'='*60}")

        try:
            project = rf.workspace(workspace).project(project_slug)
            dataset = project.version(version_num).download(
                model_format=OUTPUT_FORMAT,
                location=dest,
                overwrite=True
            )
            print(f"✅ Descargado en: {dest}")
            print(f"   📁 Archivos: {os.listdir(dest)}")
        except Exception as e:
            print(f"❌ Error descargando {project_slug}: {e}")
            print(f"   → Verifica el workspace/project slug en la URL de Roboflow Universe")


if __name__ == "__main__":
    if not API_KEY:
        print("⚠️  ERROR: No se encontró ROBOFLOW_API_KEY.")
        print("   Crea el fichero .env en la raíz del proyecto con:")
        print("   ROBOFLOW_API_KEY=rf_xxxxxxxxxxxxxx")
        print("   (El .env está en .gitignore y NO se sube a GitHub)")
    else:
        download_all()
