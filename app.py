
import streamlit as st
from onboarding import generate_onboarding_plan

st.set_page_config(
    page_title="Onboarding Assistant",
    layout="centered"
)

st.title("🚀 Onboarding Assistant 🚀")
st.write(
    "Generate a structured onboarding plan "
    "tailored to each employee."
)

st.info(
    "Prototype — the plan currently uses predefined rules, "
    "not an AI model yet."
)

st.subheader("Employee details")

job_title = st.selectbox(
    "Job title",
    ["Project Manager", "BI Analyst", "Marketing Specialist"]
)

department = st.selectbox(
    "Department",
    [
        "Project Management",
        "Data & Analytics",
        "Marketing",
        "Operations"
    ]
)

experience_level = st.selectbox(
    "Experience level",
    ["Junior", "Mid-level", "Senior"]
)

if st.button("Generate onboarding plan", type="primary"):
    tasks = generate_onboarding_plan(
        job_title,
        department,
        experience_level
    )

    st.divider()
    st.subheader("Your onboarding plan")

    st.write(f"**Job title:** {job_title}")
    st.write(f"**Department:** {department}")
    st.write(f"**Experience level:** {experience_level}")

    st.warning("Draft plan — manager review is recommended.")

    for number, task in enumerate(tasks, start=1):
        with st.expander(
            f"{number}. {task['task']}",
            expanded=True
        ):
            st.write(f"**Phase:** {task['phase']}")
            st.write(f"**Priority:** {task['priority']}")
            st.write(f"**Owner:** {task['owner']}")

            independence = task.get(
                "independence_level",
                "Not specified"
            )
            st.write(f"**Independence level:** {independence}")

            st.write("**Instructions:**")
            for instruction in task["instructions"]:
                st.write(f"- {instruction}")

            st.write(f"**Expected outcome:** {task['expected_outcome']}")
