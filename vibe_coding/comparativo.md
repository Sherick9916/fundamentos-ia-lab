# Comparativo de Modelos - Práctica Vibe Coding

**Problema planteado:** Consumir la API 'Fake Store', validar la respuesta, calcular el precio promedio, máximo y mínimo de los productos, y generar un gráfico de barras con los 5 primeros productos usando Matplotlib.

## Tabla Comparativa

| Criterio | Local general (Ollama - Llama 3.2) | Local coding (LM Studio - Qwen Coder) | Cloud coding (ChatGPT) |
| :--- | :--- | :--- | :--- |
| **Código ejecutable** | Sí, a la primera, pero con warning de márgenes en el gráfico. | Sí, pero con un bug lógico y warning de layout en consola. | Sí, funcionó de forma impecable a la primera. |
| **Errores encontrados** | Warning de Matplotlib (`Tight layout not applied`) por la longitud de los títulos. | Bug lógico: El prompt pedía graficar 5 productos, pero el código graficó los 20, causando saturación visual. | Ninguno. |
| **Iteraciones necesarias** | 1 iteración. | 1 iteración. | 1 iteración. |
| **Tiempo hasta solución** | ~54 segundos. | 86.1 segundos. | < 5 segundos (Instantáneo). |
| **Calidad/claridad del código** | Estilo procedimental básico, claro y directo. | Excelente estructura orientada a la ingeniería (uso de funciones separadas y `main()`). | Procedimental, ordenado y altamente eficiente. |
| **Documentación** | Explicación paso a paso fuera del código y comentarios redundantes línea por línea. | Comentarios básicos, pero el código se explica solo por sus nombres de funciones. | Comentarios precisos, útiles y en los lugares correctos. |
| **Pruebas sugeridas/generadas** | No sugirió validaciones extra más allá del status 200. | Incluyó bloques `try-except` para manejar errores de red o excepciones generales. | El modelo ofreció generar una versión más robusta con `try/except` al final de su respuesta. |
| **Intervención humana necesaria** | Ninguna, solo ejecutar e instalar dependencias. | Fue necesario notar que el gráfico incluyó todos los productos y no los 5 solicitados. | Ninguna. |

## Reflexión Técnica
Al comparar los modelos, es evidente la diferencia en recursos y enfoque. El modelo cloud (ChatGPT) fue el más rápido y preciso para seguir las instrucciones al pie de la letra, logrando un gráfico perfecto. Sin embargo, resulta interesante que el modelo local especializado en código (Qwen Coder) intentó aplicar mejores prácticas de ingeniería de software al modularizar la solución con funciones y bloques `try-except`, aunque paradójicamente falló en aislar los 5 productos solicitados para el gráfico. El modelo generalista local cumplió de forma básica, demostrando que es posible automatizar tareas de desarrollo sencillas sin depender de la nube, aunque a costa de un mayor tiempo de procesamiento por las limitaciones de hardware local.