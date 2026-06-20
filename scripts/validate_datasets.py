"""
Script de validación post-descarga.
Comprueba que cada dataset descargado tiene la estructura correcta para YOLOv8.

USO:
    python scripts/validate_datasets.py
"""

import os
import yaml

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
MARCAS = ["nokia", "samsung", "iphone", "motorola", "xiaomi"]

def validate_dataset(brand_path: str, brand_name: str):
    print(f"\n{'─'*50}")
    print(f"🔍 Validando: {brand_name.upper()}")
    print(f"   Ruta: {brand_path}")

    if not os.path.exists(brand_path):
        print(f"   ❌ Carpeta NO existe. Pendiente de descarga.")
        return

    contents = os.listdir(brand_path)
    if not contents:
        print(f"   ❌ Carpeta vacía. Pendiente de descarga.")
        return

    # Buscar data.yaml (lo genera Roboflow automáticamente)
    yaml_files = [f for f in contents if f.endswith(".yaml")]
    if not yaml_files:
        print(f"   ⚠️  No se encontró data.yaml")
    else:
        yaml_path = os.path.join(brand_path, yaml_files[0])
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        print(f"   ✅ data.yaml encontrado")
        print(f"      Clases ({data.get('nc', '?')}): {data.get('names', [])}")

    # Verificar splits
    for split in ["train", "valid", "test"]:
        split_path = os.path.join(brand_path, split)
        if os.path.exists(split_path):
            img_path = os.path.join(split_path, "images")
            lbl_path = os.path.join(split_path, "labels")
            n_imgs = len(os.listdir(img_path)) if os.path.exists(img_path) else 0
            n_lbls = len(os.listdir(lbl_path)) if os.path.exists(lbl_path) else 0
            print(f"   ✅ {split:6s} → {n_imgs} imágenes, {n_lbls} etiquetas")
        else:
            print(f"   ❌ {split:6s} → NO encontrado")

    total_images = sum(
        len(os.listdir(os.path.join(brand_path, s, "images")))
        for s in ["train", "valid", "test"]
        if os.path.exists(os.path.join(brand_path, s, "images"))
    )
    print(f"   📊 Total imágenes: {total_images}")


if __name__ == "__main__":
    print("=" * 50)
    print("  VALIDACIÓN DE DATASETS — data/raw/")
    print("=" * 50)

    for brand in MARCAS:
        brand_path = os.path.join(BASE_DIR, brand)
        validate_dataset(brand_path, brand)

    print(f"\n{'='*50}")
    print("Validación completada.")
