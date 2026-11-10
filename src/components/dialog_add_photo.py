
import streamlit as st
from PIL import Image
import io


# Initialize session state
if 'attendance_images' not in st.session_state:
    st.session_state.attendance_images = []

if 'processed_photos' not in st.session_state:
    st.session_state.processed_photos = set()


@st.dialog("Capture or upload photos")
def add_photos_dialog():

    st.write('Add classroom photos to scan for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = (
            "primary"
            if st.session_state.photo_tab == 'camera'
            else 'tertiary'
        )

        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'

    with t2:
        type_upload = (
            "primary"
            if st.session_state.photo_tab == 'upload'
            else 'tertiary'
        )

        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    # Camera capture
    if st.session_state.photo_tab == 'camera':

        cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')

        if cam_photo:
            image_bytes = cam_photo.getvalue()
            photo_id = hash(image_bytes)

            if photo_id not in st.session_state.processed_photos:
                image = Image.open(io.BytesIO(image_bytes)).copy()
                st.session_state.attendance_images.append(image)
                st.session_state.processed_photos.add(photo_id)

                st.toast('Photo Captured')
                st.rerun()

    # Upload multiple photos
    if st.session_state.photo_tab == 'upload':

        uploaded_files = st.file_uploader(
            'Choose image files',
            type=['jpg', 'png', 'jpeg'],
            accept_multiple_files=True,
            key='dialog_upload'
        )

        if uploaded_files:

            for f in uploaded_files:
                image_bytes = f.getvalue()
                photo_id = hash(image_bytes)

                if photo_id not in st.session_state.processed_photos:
                    image = Image.open(io.BytesIO(image_bytes)).copy()

                    st.session_state.attendance_images.append(image)
                    st.session_state.processed_photos.add(photo_id)

            st.toast('Photos uploaded successfully')
            st.rerun()

    st.divider()

    if st.button('Done', type='primary', width='stretch'):
        st.rerun()
