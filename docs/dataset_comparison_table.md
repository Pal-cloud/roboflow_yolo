# 📊 Tabla Comparativa de Datasets — Roboflow Universe
# Proyecto: Detección de logos de marcas de móviles con YOLO
# Fecha de análisis: Junio 2026

---

## 📌 Candidatos evaluados

### 🔵 NOKIA

| Campo | Candidato A | Candidato B |
|---|---|---|
| **Nombre / URL** | [Nokia – nikitas-workspace](https://universe.roboflow.com/nikitas-workspace-1jw6b/nokia-jfqln) | [nokia – aditya-chico](https://universe.roboflow.com/aditya-chico/nokia) |
| **Nº imágenes** | 300 | 28 |
| **Clases** | Nokia | headc1c2c3c4 (❌ no es logo) |
| **Split train/val/test** | ❓ verificar | ❓ verificar |
| **Formato YOLOv8** | ❓ verificar | ❓ verificar |
| **Licencia** | ❓ verificar | ❓ verificar |
| **Descargas / Estrellas** | ❓ verificar | ❓ verificar |
| **Diversidad** | ❓ verificar | ❓ verificar |
| **✅ ELEGIDO** | **← MEJOR CANDIDATO** | |

---

### 🟡 SAMSUNG

| Campo | Candidato A | Candidato B |
|---|---|---|
| **Nombre / URL** | [samsung – holland](https://universe.roboflow.com/holland/samsung-le5e2) | [samsung – prism](https://universe.roboflow.com/prism-q9krz/samsung-hpmwt) |
| **Nº imágenes** | 606 | 199 |
| **Clases** | samsung | ButtonImageText (❌ no es solo logo) |
| **Split train/val/test** | ❓ verificar | ❓ verificar |
| **Formato YOLOv8** | ❓ verificar | ❓ verificar |
| **Licencia** | ❓ verificar | ❓ verificar |
| **Descargas / Estrellas** | 11 ⭐ | ❓ verificar |
| **Diversidad** | ❓ verificar | ❓ verificar |
| **✅ ELEGIDO** | **← MEJOR CANDIDATO** | |

---

### 🍎 iPHONE / APPLE

| Campo | Candidato A | Candidato B |
|---|---|---|
| **Nombre / URL** | [Apple logo – melnyk-workspace](https://universe.roboflow.com/melnyk-workspace/apple-logo-smfdm) | [Apple Logo – ethans-space](https://universe.roboflow.com/ethans-space/apple-logo-vumbx) |
| **Nº imágenes** | 1.090 | 61 |
| **Clases** | Logo | Apple-Logo |
| **Split train/val/test** | ❓ verificar | ❓ verificar |
| **Formato YOLOv8** | ❓ verificar | ❓ verificar |
| **Licencia** | ❓ verificar | ❓ verificar |
| **Descargas / Estrellas** | 6 ⭐ | 2 ⭐ |
| **Diversidad** | ❓ verificar | ❓ verificar |
| **✅ ELEGIDO** | **← MEJOR CANDIDATO** | |

---

### 🔴 MOTOROLA

| Campo | Candidato A | Candidato B |
|---|---|---|
| **Nombre / URL** | ⚠️ No hay dataset específico de logo Motorola en Roboflow | — |
| **Nº imágenes** | — | — |
| **Clases** | — | — |
| **Notas** | Considerar crear dataset propio con imágenes de Motorola logo + LabelImg/Roboflow Annotate | |
| **Alternativa** | Buscar en Open Images Dataset o scraping manual (10-20 logos mínimo para PoC) | |

---

### 🟠 XIAOMI

| Campo | Candidato A | Candidato B |
|---|---|---|
| **Nombre / URL** | [Xiaomi Logo – boe-gpvhd](https://universe.roboflow.com/boe-gpvhd/xiaomi-logo) | [Xiaomi logo detection – hand-joint](https://universe.roboflow.com/hand-joint/xiaomi-logo-detection) |
| **Nº imágenes** | 50 | 50 |
| **Clases** | Xiaomi Logo | Xiaomi Logo |
| **Split train/val/test** | ❓ verificar | ❓ verificar |
| **Formato YOLOv8** | ❓ verificar | ❓ verificar |
| **Licencia** | ❓ verificar | ❓ verificar |
| **Descargas / Estrellas** | 2 ⭐ / 1 modelo | ❓ verificar |
| **Diversidad** | ⚠️ pocas imágenes | ⚠️ pocas imágenes |
| **Notas** | Ambos tienen pocas imágenes. Combinar ambos + data augmentation | |
| **✅ ELEGIDO** | **Combinar A + B** | |

---

## 🏆 Resumen Final de Datasets Seleccionados

| Marca | Dataset URL | Nº imágenes | Licencia | Estado descarga |
|---|---|---|---|---|
| Nokia | https://universe.roboflow.com/nikitas-workspace-1jw6b/nokia-jfqln | 300 | ❓ verificar | ⬜ pendiente |
| Samsung | https://universe.roboflow.com/holland/samsung-le5e2 | 606 | ❓ verificar | ⬜ pendiente |
| iPhone/Apple | https://universe.roboflow.com/melnyk-workspace/apple-logo-smfdm | 1.090 | ❓ verificar | ⬜ pendiente |
| Motorola | — crear dataset propio — | ~50+ | N/A | ⬜ pendiente |
| Xiaomi | https://universe.roboflow.com/boe-gpvhd/xiaomi-logo + https://universe.roboflow.com/hand-joint/xiaomi-logo-detection | 50+50 | ❓ verificar | ⬜ pendiente |

---

## ⚠️ Notas Importantes

- Todos los datasets de Roboflow Universe usan por defecto licencia **CC BY 4.0** salvo que se indique lo contrario.
- Debes verificar la licencia entrando en cada dataset → pestaña **"License"** o **"About"**.
- Para Motorola: como no hay dataset público específico, se recomienda crear uno propio usando **Roboflow Annotate** (gratuito) con imágenes descargadas de Google Images.
- Para Xiaomi: los datasets son pequeños (50 imágenes cada uno). Se recomienda combinarlos y aplicar **data augmentation** (flip, rotate, brightness) en Roboflow antes de descargar.
