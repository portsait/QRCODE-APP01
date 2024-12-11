import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Streamlit QR Code Generator App
st.title("QR Code Generator")

# User input for the QR code
url = st.text_input("Enter the text or URL to generate a QR code:")

if url:
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Convert QR code to image
    img = qr.make_image(fill_color="black", back_color="white")

    # Display the QR code in Streamlit
    st.image(img, caption="Generated QR Code", use_column_width=True)

    # Download QR code as a file
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
        label="Download QR Code",
        data=byte_im,
        file_name="qr_code.png",
        mime="image/png"
    )
