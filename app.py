import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="SkillStep IA",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 SkillStep IA")
st.subheader("Tu asistente inteligente para aprender habilidades paso a paso")

st.write(
    "SkillStep IA te ayuda a crear un plan personalizado para aprender una habilidad. "
    "Solo tenés que completar algunos datos y la inteligencia artificial generará una guía "
    "organizada con pasos, retos y recomendaciones."
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
    placeholder="Ejemplo: crear mi primera página web, mantener una conversación en inglés, diseñar un logo..."
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
    2. La app toma esa información y construye un prompt personalizado.
    3. La inteligencia artificial analiza tu situación.
    4. Recibís un plan claro con etapas, retos y consejos.
    """
)

st.info(
    "El resultado es una guía orientativa. El usuario puede adaptarla según sus necesidades, "
    "tiempos y avances personales."
)

def generar_plan(habilidad, nivel, tiempo, objetivo, plazo):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    prompt = f"""
    Actuá como un mentor experto en aprendizaje personalizado.

    Tu tarea es crear un plan de aprendizaje claro, realista y progresivo para una persona
    que quiere desarrollar una nueva habilidad.

    Datos del usuario:
    - Habilidad a aprender: {habilidad}
    - Nivel actual: {nivel}
    - Tiempo disponible por semana: {tiempo}
    - Objetivo final: {objetivo}
    - Plazo deseado: {plazo}

    Generá una respuesta con la siguiente estructura:

    1. Diagnóstico inicial del usuario.
    2. Objetivo principal reformulado de forma clara.
    3. Plan semanal dividido en etapas.
    4. Retos prácticos para cada semana.
    5. Recursos o tipos de recursos recomendados.
    6. Consejos para mantener la constancia.
    7. Indicadores para medir el progreso.

    La respuesta debe ser clara, motivadora, realista y fácil de seguir.
    No des información demasiado técnica si el usuario es principiante.
    """

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Sos un asistente experto en crear planes educativos personalizados."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return respuesta.choices[0].message.content

if st.button("Generar mi plan con IA"):
    if habilidad and objetivo:
        with st.spinner("Generando tu plan personalizado..."):
            plan = generar_plan(habilidad, nivel, tiempo, objetivo, plazo)
            st.success("Plan generado correctamente")
            st.markdown(plan)
    else:
        st.warning("Completá al menos la habilidad y el objetivo final para generar el plan.")