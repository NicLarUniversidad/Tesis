# Proyecto de tesina

## Requerimientos

- Python 3
- LM Studio

## Proceso

1. A través de prompts de referencia, generar código. (Text-to-Code | T2T)
   1. Tomar métricas. &#x2611; :heavy_check_mark:
      1. BLEU &#x2611; :heavy_check_mark:
      2. CodeBLEU &#x2611; :heavy_check_mark:
      3. Exact match &#x2611; :heavy_check_mark:
   2. Guardar resultados en archivo CSV. &#x2611; :heavy_check_mark:
2. Por cada estrategia de prompt engineering alterar los prompts y repetir el paso 1 con el prompt modificado.
3. Comparar, buscar estrategias que hayan mejorado las métricas.
4. Implementar el primer prototipo con esas estrategias.
5. Probar estrategias de Code-to-Code (C2C).
6. Buscar estrategias que C2C que hayan mejorado las métricas.
7. Implementar el segundo prototipo.
8. Probar prototipos con los demás datasets.