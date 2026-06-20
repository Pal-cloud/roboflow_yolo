# 🔍 Detección de Logos de Marcas de Móviles con YOLOv8

Proyecto de Computer Vision para detectar logos de marcas en imágenes y vídeos, desarrollado con YOLOv8 y datasets obtenidos de Roboflow Universe.

---

## 🎯 Objetivo

Entrenar un modelo de detección de objetos capaz de reconocer logos de **5 marcas de móviles**:

| Marca | Logo detectado |
|---|---|
| Nokia | Logo "Nokia" (texto azul) |
| Samsung | Logo "Samsung" (texto azul) |
| Apple / iPhone | Logo manzana mordida |
| Motorola | Logo "M" / "Batwing" |
| Xiaomi | Logo "MI" |

---

## 📁 Estructura del proyecto

```
roboflow_yolo/
├── data/
│   └── raw/               # Datasets descargados de Roboflow (YOLOv8 format)
│       ├── nokia/
│       ├── samsung/
│       ├── iphone/
│       ├── motorola/
│       └── xiaomi/
├── docs/
│   ├── dataset_checklist.md         # Criterios de validación de datasets
│   └── dataset_comparison_table.md  # Tabla comparativa de candidatos
├── scripts/
│   ├── download_datasets.py   # Descarga automática desde Roboflow API
│   └── validate_datasets.py   # Validación post-descarga
├── requirements.txt
└── README.md
```

---

## 📦 Datasets seleccionados

| Marca | Dataset | URL | Imágenes | Licencia |
|---|---|---|---|---|
| Nokia | Nokia – nikitas-workspace | https://universe.roboflow.com/nikitas-workspace-1jw6b/nokia-jfqln | ~300 | CC BY 4.0 |
| Samsung | samsung – holland | https://universe.roboflow.com/holland/samsung-le5e2 | ~606 | CC BY 4.0 |
| iPhone/Apple | Apple logo – melnyk-workspace | https://universe.roboflow.com/melnyk-workspace/apple-logo-smfdm | ~1.090 | CC BY 4.0 |
| Motorola | *(dataset propio)* | — | ~50+ | N/A |
| Xiaomi | Xiaomi Logo – boe-gpvhd | https://universe.roboflow.com/boe-gpvhd/xiaomi-logo | ~50 | CC BY 4.0 |

> **Nota Motorola:** No existe un dataset público específico de logo Motorola en Roboflow Universe.  
> Se creará un dataset propio usando **Roboflow Annotate** con imágenes obtenidas manualmente.

> **Nota Xiaomi:** El dataset tiene pocas imágenes (~50). Se aplicará **data augmentation** (flip horizontal, rotación ±15°, brillo/contraste) en Roboflow antes de descargar para ampliar el dataset.

### 📜 Licencias

Todos los datasets públicos de Roboflow Universe se publican bajo licencia **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** (Creative Commons Attribution 4.0 International) salvo indicación contraria en la página del dataset.

- **CC BY 4.0** permite: usar, copiar, adaptar y redistribuir con fines educativos y comerciales, siempre que se cite la fuente.
- Uso en este proyecto: **educativo / proof of concept**. ✅ Compatible.

Para verificar la licencia exacta de cada dataset:
1. Entra en la URL del dataset en Roboflow Universe.
2. Haz click en la pestaña **"License"** o busca en la sección **"About"**.

---

## 🚀 Instalación y uso

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar API Key de Roboflow

Crea una cuenta gratuita en [app.roboflow.com](https://app.roboflow.com/), ve a **Settings → API Key** y copia tu clave.

Edita `scripts/download_datasets.py` y reemplaza:
```python
API_KEY = "TU_API_KEY_AQUI"
```

### 3. Descargar datasets

```bash
python scripts/download_datasets.py
```

Los datasets se guardan automáticamente en `data/raw/<marca>/` en formato YOLOv8.

### 4. Validar datasets descargados

```bash
python scripts/validate_datasets.py
```

Comprueba que cada dataset tiene la estructura correcta: splits train/valid/test, imágenes y etiquetas.

---

## 📊 Proceso de selección de datasets

Ver documentación detallada en:
- [`docs/dataset_checklist.md`](docs/dataset_checklist.md) — criterios de validación
- [`docs/dataset_comparison_table.md`](docs/dataset_comparison_table.md) — tabla comparativa de candidatos

---

## 🛠️ Tecnologías

- **Python 3.10+**
- **YOLOv8** (Ultralytics)
- **Roboflow** API
- **OpenCV** (procesado de vídeo)

---

## 👥 Equipo

Proyecto de Computer Vision — Bootcamp IA  
Entregable: Nivel Esencial → detección de logos en imágenes con bounding box
