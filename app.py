import streamlit as st

st.set_page_config(
    page_title="SkillStep IA",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 SkillStep IA")
st.subheader("Tu asistente inteligente para aprender habilidades paso a paso")

st.write(
    "SkillStep IA te ayuda a crear un plan personalizado para aprender una habilidad. "
    "Completás algunos datos y la aplicación genera una guía organizada con pasos, "
    "retos y recomendaciones."
)

st.divider()

st.header("Crear mi plan de aprendizaje")

habilidad = st.text_input(
    "¿Qué habilidad querés aprender?",
    placeholder="Ejemplo: programación web, inglés, diseño gráfico, edición de video..."
)

nivel = st.selectbox(
    "¿Cuál es tu nivel actual?",
    ["Principiante", "Intermedio", "Avanzado"]
)

tiempo = st.selectbox(
    "¿Cuánto tiempo podés dedicar por semana?",
    ["1 a 2 horas", "3 a 5 horas", "6 a 10 horas", "Más de 10 horas"]
)

objetivo = st.text_area(
    "¿Cuál es tu objetivo final?",
    placeholder="Ejemplo: crear mi primera página web, mantener una conversación en inglés..."
)

plazo = st.selectbox(
    "¿En cuánto tiempo querés lograrlo?",
    ["2 semanas", "1 mes", "2 meses", "3 meses", "6 meses"]
)

st.divider()

st.header("Cómo funciona")

st.write(
    """
    1. Completás los datos sobre la habilidad que querés aprender.
    2. La app analiza tu nivel, tiempo disponible y objetivo.
    3. Se genera una salida dirigida basada en un prompt estructurado.
    4. Recibís un plan claro con etapas, retos y consejos.
    """
)

st.info(
    "Esta versión académica simula una respuesta de IA a partir de un prompt estructurado, "
    "sin utilizar una API paga. La aplicación puede integrarse con un modelo de IA externo "
    "en una futura versión."
)


def generar_plan(habilidad, nivel, tiempo, objetivo, plazo):
    if plazo == "2 semanas":
        semanas = 2
    elif plazo == "1 mes":
        semanas = 4
    elif plazo == "2 meses":
        semanas = 8
    elif plazo == "3 meses":
        semanas = 12
    else:
        semanas = 24

    if nivel == "Principiante":
        enfoque = "empezar desde los conceptos básicos, evitando avanzar demasiado rápido."
        dificultad = "básicos"
    elif nivel == "Intermedio":
        enfoque = "reforzar lo que ya sabés y aplicar la habilidad en ejercicios prácticos."
        dificultad = "intermedios"
    else:
        enfoque = "perfeccionar la técnica, trabajar con desafíos complejos y mejorar la autonomía."
        dificultad = "avanzados"

    return f"""
## Plan personalizado para aprender {habilidad}

### 1. Diagnóstico inicial

Tu nivel actual es **{nivel}** y contás con **{tiempo} por semana** para practicar.  
Tu objetivo principal es: **{objetivo}**.  
El plazo estimado para alcanzar este objetivo es de **{plazo}**.

Según estos datos, lo más importante es {enfoque}

---

### 2. Objetivo principal reformulado

Desarrollar la habilidad de **{habilidad}** de manera progresiva, práctica y organizada, hasta poder lograr el siguiente objetivo:

**{objetivo}**

---

### 3. Plan de aprendizaje

#### Etapa 1: Introducción y organización

- Investigar qué conocimientos básicos necesitás para aprender {habilidad}.
- Buscar ejemplos simples relacionados con tu objetivo.
- Armar una lista de temas principales.
- Definir días y horarios de práctica según tu disponibilidad.

#### Etapa 2: Práctica guiada

- Realizar ejercicios {dificultad}.
- Seguir tutoriales o guías paso a paso.
- Anotar dudas y errores frecuentes.
- Repetir las prácticas más importantes hasta ganar confianza.

#### Etapa 3: Aplicación práctica

- Crear una actividad, ejercicio o mini proyecto relacionado con tu objetivo.
- Aplicar lo aprendido en una situación real.
- Comparar tu resultado con ejemplos de referencia.
- Mejorar los puntos débiles detectados.

#### Etapa 4: Revisión y mejora

- Revisar todo lo trabajado.
- Corregir errores.
- Mejorar la presentación o calidad del resultado final.
- Definir próximos pasos para seguir avanzando después del plazo inicial.

---

### 4. Retos prácticos sugeridos

- Realizar al menos una práctica semanal relacionada con {habilidad}.
- Guardar evidencia de tu progreso.
- Explicar con tus palabras lo aprendido al final de cada semana.
- Hacer una autoevaluación simple: qué entendí, qué me costó y qué debo mejorar.
- Crear un resultado final relacionado con: **{objetivo}**.

---

### 5. Recursos recomendados

- Videos introductorios.
- Guías paso a paso.
- Documentación o material básico.
- Ejercicios prácticos.
- Comunidades, foros o grupos relacionados con {habilidad}.
- Ejemplos reales para comparar tu avance.

---

### 6. Consejos para mantener la constancia

- Dividí el objetivo en tareas pequeñas.
- No intentes aprender todo de golpe.
- Practicá de forma regular, aunque sea poco tiempo.
- Medí tu progreso semanalmente.
- Ajustá el plan si tu disponibilidad cambia.
- Priorizá la práctica sobre la teoría excesiva.

---

### 7. Indicadores para medir el progreso

Podés medir tu avance observando:

- Cantidad de prácticas realizadas.
- Nivel de confianza con los conceptos.
- Capacidad para explicar lo aprendido.
- Reducción de errores.
- Avance concreto hacia tu objetivo: **{objetivo}**.
- Resultado final conseguido al terminar el plazo de **{plazo}**.

---

### 8. Recomendación final

Durante aproximadamente **{semanas} semanas**, intentá mantener una rutina constante.  
Lo más importante no es avanzar perfecto, sino avanzar de forma ordenada y sostenida.
"""


if st.button("Generar mi plan"):
    if habilidad and objetivo:
        with st.spinner("Generando tu plan personalizado..."):
            plan = generar_plan(habilidad, nivel, tiempo, objetivo, plazo)
            st.success("Plan generado correctamente")
            st.markdown(plan)
    else:
        st.warning("Completá al menos la habilidad y el objetivo final para generar el plan.")