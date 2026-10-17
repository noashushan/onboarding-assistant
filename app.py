
import streamlit as st
from onboarding import generate_onboarding_plan

from io import BytesIO
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule



st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #423340;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #423340;
    font-weight: 500;
}

.stApp {
    background: linear-gradient(145deg, #FFF7F8 0%, #FFF9FC 55%, #F8F3FC 100%);
}

.block-container {
    max-width: 1100px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

div[data-testid="stAlert"] {
    border-radius: 16px;
    border: 1px solid #F2D5DF;
}

div[data-testid="stExpander"] {
    background-color: rgba(255, 255, 255, 0.88);
    border: 1px solid #F0DCE4;
    border-radius: 16px;
    overflow: hidden;
}

div[data-testid="stProgressBar"] > div {
    background-color: #F3E5EB;
    border-radius: 999px;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #F2B8C9, #E9CDEB);
    border-radius: 999px;
}

div.stButton > button {
    background: #EFB9CA;
    color: #423340;
    border: 1px solid #EFB9CA;
    border-radius: 14px;
    font-weight: 600;
    padding: 0.65rem 1.3rem;
    transition: all 0.2s ease;
}


div.stButton > button {
    background: linear-gradient(135deg, #F6D5E0, #EFB9CA);
    color: #493744;
    border: 1px solid #EAB4C7;
    border-radius: 16px;
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    padding: 0.8rem 1.6rem;
    box-shadow: 0 5px 14px rgba(194, 132, 158, 0.16);
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #F0C2D2, #E7A5BC);
    color: #493744;
    border-color: #E7A5BC;
    box-shadow: 0 8px 20px rgba(194, 132, 158, 0.25);
    transform: translateY(-2px);
}

div.stButton > button:active {
    transform: translateY(0);
}


div[data-testid="stSelectbox"] > div > div {
    background-color: #FFFFFF;
    border-radius: 12px;
    border-color: #EBDDE3;
}

.hero {
    background: linear-gradient(135deg, #FBE8EE, #F7F0FA);
    border: 1px solid #F0DCE5;
    border-radius: 24px;
    padding: 2.5rem;
    margin-bottom: 1.8rem;
}

.hero-eyebrow {
    color: #A36F89;
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    margin-bottom: 1rem;
}

.hero h1 {
    font-family: 'DM Sans', sans-serif !important;
    font-size: clamp(2.2rem, 6vw, 4rem);
    line-height: 1.1;
    letter-spacing: -0.04em;
    margin: 0 0 1rem 0;
    color: #493744;
    font-weight: 700;
}

.hero p {
    color: #796775;
    font-size: 1.05rem;
    margin: 0;
    line-height: 1.7;
}

.section-heading {
    margin: 2rem 0 1.5rem 0;
}

.section-label {
    display: inline-block;
    color: #A36F89;
    background: #F9E5EC;
    border-radius: 999px;
    padding: 0.35rem 0.8rem;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
}

.section-heading h2 {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 2rem;
    font-weight: 700;
    color: #493744;
    margin: 0.8rem 0 0.4rem 0;
}

.section-heading p {
    color: #796775;
    font-size: 0.98rem;
    margin: 0;
}

.priority-badge {
    display: inline-block;
    padding: 0.3rem 0.75rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.02em;
}

.priority-high {
    background: #F7D4DF;
    color: #8F3F60;
    border: 1px solid #EDB8CA;
}

.priority-medium {
    background: #FCEAF0;
    color: #98647B;
    border: 1px solid #F2D7E2;
}

.priority-low {
    background: #EEE7F8;
    color: #765B98;
    border: 1px solid #DDD0EF;
}



</style>
""", unsafe_allow_html=True)


st.set_page_config(
    page_title="Onboarding Assistant",
    layout="centered"
)


st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">A structured beginning.</div>
    <h1>Onboarding Process Generator</h1>
    <p>Create a thoughtful onboarding experience,
    tailored to every new hire.</p>
</div>
""", unsafe_allow_html=True)





st.markdown("""
<div class="section-heading">
    <span class="section-label">STEP 01</span>
    <h2>Let's meet your new hire</h2>
    <p>A few details will help us create a more relevant onboarding plan.</p>
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2, gap="large")

with col1:
    job_title = st.selectbox(
        "Job title",
        ["Project Manager", "BI Analyst", "Marketing Specialist"]
    )

with col2:
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
    st.session_state.tasks = generate_onboarding_plan(
        job_title,
        department,
        experience_level
    )
    st.session_state.completed_tasks = {}

if "tasks" in st.session_state:
    tasks = st.session_state.tasks
    
    plan_text = "ONBOARDING PLAN\n"
    plan_text += "=" * 40 + "\n\n"

    plan_text += f"Job title: {job_title}\n"
    plan_text += f"Department: {department}\n"
    plan_text += f"Experience level: {experience_level}\n\n"

    for number, task in enumerate(tasks, start=1):
        plan_text += f"{number}. {task['task']}\n"
        plan_text += f"   Phase: {task['phase']}\n"
        plan_text += f"   Priority: {task['priority']}\n"
        plan_text += f"   Owner: {task['owner']}\n"
        plan_text += "   Instructions:\n"

        for instruction in task["instructions"]:
            plan_text += f"   - {instruction}\n"

        plan_text += (
            f"   Expected outcome: "
            f"{task['expected_outcome']}\n\n"
        )

    
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Onboarding Plan"

    headers = [
        "Phase",
        "Task",
        "Priority",
        "Owner",
        "Instructions",
        "Expected Outcome",
        "Status"
    ]
    sheet.append(headers)

    for number, task in enumerate(tasks, start=1):
        status = (
            "Completed"
            if st.session_state.get(f"completed_{number}", False)
            else "Not started"
        )

        sheet.append([
            task["phase"],
            task["task"],
            task["priority"],
            task["owner"],
            "\n".join(task["instructions"]),
            task["expected_outcome"],
            status
        ])

    header_fill = PatternFill(
        fill_type="solid",
        fgColor="E9E1F5"
    )

    for cell in sheet[1]:
        cell.font = Font(bold=True, color="423340")
        cell.fill = header_fill
        cell.alignment = Alignment(
            vertical="center",
            wrap_text=True
        )

    column_widths = [16, 32, 14, 20, 48, 48, 16]

    for column_number, width in enumerate(column_widths, start=1):
        sheet.column_dimensions[
            get_column_letter(column_number)
        ].width = width

    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(
                vertical="top",
                wrap_text=True
            )
    
    # Add a dropdown menu for task status
    status_dropdown = DataValidation(
        type="list",
        formula1='"Not started,In progress,Completed"',
        allow_blank=False
    )
    status_dropdown.error = "Please select a status from the dropdown."
    status_dropdown.errorTitle = "Invalid status"
    status_dropdown.prompt = "Select the current task status."
    status_dropdown.promptTitle = "Task status"
    sheet.add_data_validation(status_dropdown)

    for row_number in range(2, sheet.max_row + 1):
        status_dropdown.add(f"G{row_number}")

    # Add automatic colors based on status
    status_colors = {
        "Not started": ("FCE4D6", "9C0006"),
        "In progress": ("FFF2CC", "7F6000"),
        "Completed": ("E2F0D9", "375623")
    }

    for status, (background_color, font_color) in status_colors.items():
        sheet.conditional_formatting.add(
            f"G2:G{sheet.max_row}",
            CellIsRule(
                operator="equal",
                formula=[f'"{status}"'],
                fill=PatternFill(
                    fill_type="solid",
                    fgColor=background_color
                ),
                font=Font(color=font_color)
            )
        )

    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = sheet.dimensions

    excel_file = BytesIO()
    workbook.save(excel_file)
    excel_file.seek(0)

    
    st.markdown("### Export your onboarding plan")
    st.caption("Choose the format that works best for you.")

    col_txt, col_excel = st.columns(2, gap="medium")

    with col_txt:
        st.download_button(
            label="📄 Download as TXT",
            data=plan_text,
            file_name="onboarding_plan.txt",
            mime="text/plain",
            use_container_width=True
        )

    
    with col_excel:
        st.download_button(
            label="📊 Download as Excel (.xlsx)",
            data=excel_file.getvalue(),
            file_name="onboarding_plan.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )




    st.divider()
    st.subheader("Your onboarding plan")

    st.write(f"**Job title:** {job_title}")
    st.write(f"**Department:** {department}")
    st.write(f"**Experience level:** {experience_level}")

    st.warning("Draft plan — manager review is recommended.")

    total_tasks = len(tasks)
    completed_count = sum(
    st.session_state.get(f"completed_{number}", False)
    for number in range(1, total_tasks + 1)
)
    progress = completed_count / total_tasks if total_tasks else 0

    st.divider()
    st.subheader("Onboarding progress")
    st.progress(progress)
    st.write(f"{completed_count} of {total_tasks} tasks completed ({progress:.0%})")
    if progress == 1:
        st.success("Congratulations! Onboarding completed successfully!")
        st.balloons()

    for number, task in enumerate(tasks, start=1):
        task_key = f"completed_{number}"

        completed = st.checkbox(
            f"Mark as completed — {task['task']}",
            key=task_key,
            value=st.session_state.completed_tasks.get(number, False)
        )

        st.session_state.completed_tasks[number] = completed
        


        with st.expander(
            f"{number}. {task['task']}",
            expanded=True
        ):
            st.write(f"**Phase:** {task['phase']}")
            priority = task["priority"].lower()

            if priority == "high":
                priority_class = "priority-high"
            elif priority == "medium":
                priority_class = "priority-medium"
            else:
                priority_class = "priority-low"

            st.markdown(
                f'<span class="priority-badge {priority_class}">'
                f'Priority · {task["priority"]}'
                '</span>',
                unsafe_allow_html=True
)

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

