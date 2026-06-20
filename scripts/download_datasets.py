"""
Script de descarga de datasets desde Roboflow Universe.
Requiere: pip install roboflow

USO:
    1. Crea una cuenta gratuita en https://app.roboflow.com/
    2. Ve a Settings > API Key y copia tu API key
    3. Ejecuta: python scripts/download_datasets.py

Los datasets se guardan en data/raw/<marca>/
"""

from roboflow import Roboflow
import os

# ─── CONFIGURACIÓN ────────────────────────────────────────────────────────────
API_KEY = "TU_API_KEY_AQUI"   # <-- reemplaza con tu API key de Roboflow
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
    if API_KEY == "TU_API_KEY_AQUI":
        print("⚠️  ERROR: Debes añadir tu API Key de Roboflow en este script.")
        print("   Ve a https://app.roboflow.com/ → Settings → API Key")
    else:
        download_all()
