import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2
from streamlit_drawable_canvas import st_canvas
from tensorflow.keras.models import load_model


def main():

    # Load model
    model = load_model('model.keras')

    st.write('## Handwritten digits recognizer')

    st.write('##### Please draw a number:')

    # Create a canvas component
    canvas_result = st_canvas(
        stroke_width=20,
        update_streamlit=True,
        height=200,
        width=200,
        key="canvas",
    )

    st.write('##### Predicted number:')

    if np.array_equal(canvas_result.image_data[:, :, -1], np.zeros((200, 200))):
        st.write("Canvas is empty.")
    else:

        # Convert 3D NumPy array (RGBA) to 2D NumPy array (Grayscale)
        # extracting the Alpha value (last value along the third axis)

        image = canvas_result.image_data[:, :, -1]

        resized_image = cv2.resize(image, (28, 28))

        normalized_image = resized_image / 255.0

        predict = normalized_image.reshape(1, 28, 28)

        prediction = model.predict(predict)

        fig, ax = plt.subplots()
        ax.bar(range(10), prediction[0]*100, color="#777777")
        ax.set_xticks(range(10))
        ax.set_ylabel("Confidence %")
        st.pyplot(fig)
        


if __name__ == '__main__':
    main()