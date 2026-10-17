
import streamlit as st

st.set_page_config(
    page_title="AI Onboarding Assistant",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 AI Onboarding Assistant")
st.write(
    "Create a structured onboarding plan "
    "for your new employee."
)

st.info(
    "This is a prototype. The plan is generated "
    "using predefined rules, not AI yet."
)

# User inputs
st.subheader("Employee details")

job_title = st.selectbox(
    "Job title",
    [
        "Project Manager",
        "BI Analyst",
        "Marketing Specialist"
    ]
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

# Generate the onboarding plan
if st.button("Generate onboarding plan", type="primary"):

    tasks = [
        {
            "task": "Prepare the employee's starting materials",
            "phase": "Before Day 1",
            "priority": "High",
            "owner": "Manager",
            "outcome": "Starting materials are ready."
        },
        {
            "task": "Clarify responsibilities and expectations",
            "phase": "Day 1",
            "priority": "High",
            "owner": "Manager",
            "outcome": "The employee understands their responsibilities."
        },
        {
            "task": "Complete an initial work task",
            "phase": "Week 1",
            "priority": "High",
            "owner": "New employee",
            "outcome": "The employee completes an initial task."
        },
        {
            "task": "Review progress and remaining questions",
            "phase": "Days 8-30",
            "priority": "Medium",
            "owner": "Manager",
            "outcome": "Progress and next steps are agreed."
        }
    ]

    # Adapt the plan to the experience level
    independence_levels = {
        "Junior": "Guided",
        "Mid-level": "Semi-independent",
        "Senior": "Independent"
    }

    instructions_by_level = {
        "Junior": (
            "Complete this task with guidance and ask "
            "questions whenever needed."
        ),
        "Mid-level": (
            "Complete the task independently where possible "
            "and request reviews when needed."
        ),
        "Senior": (
            "Take ownership of the task and identify "
            "opportunities for improvement."
        )
    }

    # Customize one task according to the selected role
    if job_title == "Project Manager":
        tasks[2]["task"] = "Review the project plan and milestones"
        tasks[2]["outcome"] = (
            "The employee understands the project scope and timeline."
        )

    elif job_title == "BI Analyst":
        tasks[2]["task"] = "Explore the available data and reports"
        tasks[2]["outcome"] = (
            "The employee understands the main data sources and reports."
        )

    elif job_title == "Marketing Specialist":
        tasks[2]["task"] = "Review current marketing activities"
        tasks[2]["outcome"] = (
            "The employee understands current marketing priorities."
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
            st.write(
                "**Independence level:** "
                f"{independence_levels[experience_level]}"
            )
            st.write("**Instructions:**")
            st.write(instructions_by_level[experience_level])
            st.write(f"**Expected outcome:** {task['outcome']}")
