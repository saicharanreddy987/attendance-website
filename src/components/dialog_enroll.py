
import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase


@st.dialog("Enroll in Subject")
def enroll_dialog():

    st.write(
        "Enter the subject code provided by your teacher to enroll."
    )

    join_code = st.text_input(
        "Subject Code",
        placeholder="Eg. CS101",
        key="enroll_subject_code"
    )

    if st.button(
        "Enroll now",
        type="primary",
        width="stretch",
        key="confirm_enrollment"
    ):

        # Validate subject code
        if not join_code or not join_code.strip():
            st.warning("Please enter a subject code.")

        else:
            try:
                code = join_code.strip()

                # Find subject using subject code
                res = (
                    supabase.table("subjects")
                    .select("subject_id, name, subject_code")
                    .eq("subject_code", code)
                    .execute()
                )

                if not res.data:
                    st.error(
                        "Invalid subject code. Please check with your teacher."
                    )

                else:
                    subject = res.data[0]

                    # Get logged-in student ID
                    if "student_data" not in st.session_state:
                        st.error("Student session not found. Please log in again.")

                    else:
                        student_id = st.session_state.student_data.get(
                            "student_id"
                        )

                        if student_id is None:
                            st.error("Student ID not found. Please log in again.")

                        else:
                            subject_id = subject["subject_id"]

                            # Check existing enrollment
                            check = (
                                supabase.table("subject_students")
                                .select("subject_id")
                                .eq("subject_id", subject_id)
                                .eq("student_id", student_id)
                                .execute()
                            )

                            if check.data:
                                st.warning(
                                    "You are already enrolled in this subject."
                                )

                            else:
                                # Enroll student
                                result = enroll_student_to_subject(
                                    student_id, subject_id
                                )

                                if result is None or result is False:
                                    st.error(
                                        "Enrollment failed. Please try again."
                                    )

                                else:
                                    st.success(
                                        f"Successfully enrolled in {subject['name']}!"
                                    )
                                    st.rerun()

            except Exception as e:
                st.error(f"Enrollment failed: {e}")
