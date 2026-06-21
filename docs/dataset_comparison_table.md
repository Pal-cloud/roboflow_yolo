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
| **Clases** | Nokia ✅ | head, c1, c2, c3, c4 ⚠️ (piezas, no logo) |
| **Versiones exportables** | ❌ 0 versiones — no descargable por API | ✅ 5 versiones disponibles |
| **Split train/val/test** | ❓ no verificable (sin versión) | ✅ incluido en versión 5 |
| **Formato YOLOv8** | ❌ no disponible | ✅ disponible |
| **Licencia** | ✅ CC BY 4.0 | ✅ CC BY 4.0 |
| **Descargas / Estrellas** | 0 ⭐ | 1 descarga |
| **Notas** | Mejor contenido pero no descargable. Para usarlo: Fork en Roboflow → generar versión manualmente | Clases no son logo Nokia, pero es el único descargable por API |
| **✅ ELEGIDO** | — | **← ELEGIDO (único descargable)** |

> ⚠️ **Acción pendiente**: Para obtener el dataset Nokia de 300 imágenes con el logo real, entra en  
> https://universe.roboflow.com/nikitas-workspace-1jw6b/nokia-jfqln → **Fork Dataset** → genera versión YOLOv8 → descarga manualmente en `data/raw/nokia/`.

---

### 🟡 SAMSUNG

| Campo | Candidato A | Candidato B |
|---|---|---|
| **Nombre / URL** | [samsung – holland](https://universe.roboflow.com/holland/samsung-le5e2) | [samsung – prism](https://universe.roboflow.com/prism-q9krz/samsung-hpmwt) |
| **Nº imágenes** | 606 | 199 |
| **Clases** | samsung ✅ | ButtonImageText ❌ (no es logo) |
| **Versiones exportables** | ✅ 2 versiones | ❓ sin verificar |
| **Split train/val/test** | ✅ incluido | ❓ sin verificar |
| **Formato YOLOv8** | ✅ disponible | ❓ sin verificar |
| **Licencia** | ✅ CC BY 4.0 | ❓ sin verificar |
| **Descargas / Estrellas** | 13 descargas | — |
| **Diversidad** | ✅ variedad de fondos y ángulos | ⚠️ pocas imágenes |
| **✅ ELEGIDO** | **← ELEGIDO** | |

---

### 🍎 iPHONE / APPLE

| Campo | Candidato A | Candidato B |
|---|---|---|
| **Nombre / URL** | [Apple logo – melnyk-workspace](https://universe.roboflow.com/melnyk-workspace/apple-logo-smfdm) | [Apple Logo – ethans-space](https://universe.roboflow.com/ethans-space/apple-logo-vumbx) |
| **Nº imágenes** | 1.091 | 61 |
| **Clases** | Logo ✅ | Apple-Logo ✅ |
| **Versiones exportables** | ✅ 4 versiones | ✅ disponible |
| **Split train/val/test** | ✅ incluido | ❓ sin verificar |
| **Formato YOLOv8** | ✅ disponible | ❓ sin verificar |
| **Licencia** | ✅ CC BY 4.0 | ✅ CC BY 4.0 |
| **Descargas / Estrellas** | 11 descargas, 6 ⭐ | 2 ⭐ |
| **Diversidad** | ✅ muy buena (1091 imgs) | ⚠️ pocas imágenes |
| **✅ ELEGIDO** | **← ELEGIDO** | |

---

### 🔴 MOTOROLA

| Campo | Resultado |
|---|---|
| **Búsqueda en Roboflow** | ❌ No existe dataset específico de logo Motorola |
| **Alternativa** | Crear dataset propio con Roboflow Annotate |
| **Pasos** | 1. Recopila 50+ imágenes del logo Motorola (Google Images) → 2. Sube a [app.roboflow.com](https://app.roboflow.com/) → 3. Anota con Roboflow Annotate → 4. Genera versión YOLOv8 → 5. Descarga en `data/raw/motorola/` |
| **Estado** | ⬜ Pendiente — excluido de la descarga automática |

---

### 🟠 XIAOMI

| Campo | Resultado |
|---|---|
| **Mejor candidato** | [Xiaomi Logo – boe-gpvhd](https://universe.roboflow.com/boe-gpvhd/xiaomi-logo) |
| **Nº imágenes** | 50 |
| **Versiones exportables** | ✅ 1 versión + 1 modelo entrenado |
| **Problema** | Dataset muy pequeño (50 imágenes) — necesita augmentation |
| **Estado** | ⬜ Pendiente — excluido de la descarga automática por tamaño insuficiente |

---

## 🏆 Resumen Final — Datasets Descargados

| Marca | Dataset | URL | Imágenes | Versión usada | Licencia | Estado |
|---|---|---|---|---|---|---|
| Nokia | nokia – aditya-chico | https://universe.roboflow.com/aditya-chico/nokia | 28 | v5 | CC BY 4.0 | ✅ Descargado en `data/raw/nokia/` |
| Samsung | samsung – holland | https://universe.roboflow.com/holland/samsung-le5e2 | 606 | v2 | CC BY 4.0 | ✅ Descargado en `data/raw/samsung/` |
| iPhone/Apple | Apple logo – melnyk-workspace | https://universe.roboflow.com/melnyk-workspace/apple-logo-smfdm | 1.091 | v4 | CC BY 4.0 | ✅ Descargado en `data/raw/iphone/` |
| Motorola | — dataset propio — | — | — | — | — | ⬜ Pendiente creación manual |
| Xiaomi | Xiaomi Logo – boe-gpvhd | https://universe.roboflow.com/boe-gpvhd/xiaomi-logo | 50 | v1 | CC BY 4.0 | ⬜ Pendiente (dataset pequeño) |

---

## 📜 Licencias

Todos los datasets públicos descargados están bajo licencia **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** (Creative Commons Attribution 4.0 International).

**CC BY 4.0 permite:** usar, copiar, adaptar y redistribuir el dataset con cualquier fin (incluido educativo y comercial), siempre que se cite la fuente original.

**Uso en este proyecto:** educativo / proof of concept ✅ Compatible con CC BY 4.0.

### Citas de los datasets

```bibtex
@misc{ nokia_dataset,
  title = { nokia Dataset },
  author = { aditya },
  url = { https://universe.roboflow.com/aditya-chico/nokia },
  publisher = { Roboflow },
  year = { 2022 },
}

@misc{ samsung-le5e2_dataset,
  title = { samsung Dataset },
  author = { holland },
  url = { https://universe.roboflow.com/holland/samsung-le5e2 },
  publisher = { Roboflow },
  year = { 2022 },
}

@misc{ apple-logo-smfdm_dataset,
  title = { Apple logo Dataset },
  author = { Melnyk workspace },
  url = { https://universe.roboflow.com/melnyk-workspace/apple-logo-smfdm },
  publisher = { Roboflow },
  year = { 2024 },
}
```
