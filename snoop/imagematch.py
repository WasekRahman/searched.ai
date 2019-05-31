import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import urllib.request
import cv2
 

matched = ['']
# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
    # return the image
    return image

def image_search(path,path1):
    #path = url_to_image(path)
    #path1 = url_to_image(path1)
    image_of_wasek = face_recognition.load_image_file(path)
    wasek_face_encoding = face_recognition.face_encodings(image_of_wasek)[0]

    #  Create arrays of encodings and names
    known_face_encodings = [
        wasek_face_encoding
    ]

    known_face_names = [
        "Wasek Rahman"
    ]

    people = {'Wasek Rahman': {'Age': '21', 'House': 'Dhaka', 'Last Seen': 'Banani'}
              }

    # Load test image to find faces in
    test_image = face_recognition.load_image_file(
        path1)

    # Find faces in test image
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    # Convert to PIL format
    pil_image = Image.fromarray(test_image)

    # Create a ImageDraw instance
    # draw = ImageDraw.Draw(pil_image)

    # Loop through faces in test image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown Person"

        # If match
        if True in matches:
            first_match_index = matches.index(True)
            #pil_image.show()
            name = known_face_names[first_match_index]
            matches.append([name,path,path1])
            return matches
        else:
            return "No"
        # Draw box

       
import glob
for file in glob.glob("C:\\Users\\Dell\\search\\media\\images\\*.jpg"):
    for file1 in glob.glob("C:\\Users\\Dell\\search\\media\\imagesunknown\\*.jpg"):
        print(image_search(file,file1))