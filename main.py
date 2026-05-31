import speech_recognition as sr
import pyttsx3
import mysql.connector
import re
from datetime import datetime

# -------------------- TEXT TO SPEECH SETUP --------------------

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)


def speak(text):
    print("\nAI Assistant :", text)
    engine.say(text)
    engine.runAndWait()


# -------------------- DATABASE CONNECTION --------------------

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="transport_db"
    )

    cursor = db.cursor()

    print("Database connected successfully")

except mysql.connector.Error as err:
    print(f"Database Error : {err}")
    exit()


# -------------------- SPEECH INPUT --------------------

def take_voice_input():

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 1

    try:
        with sr.Microphone() as source:

            speak("Welcome to Air Driven Transport Assistant")
            speak("Please say your destination")

            print("Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            print("Recognizing...")

            text = recognizer.recognize_google(audio)

            text = text.lower()

            print("User Said :", text)

            return text

    except sr.UnknownValueError:
        speak("Sorry, I could not understand your voice")
        return None

    except sr.RequestError:
        speak("Internet connection problem")
        return None

    except sr.WaitTimeoutError:
        speak("No speech detected")
        return None

    except Exception as e:
        print("Error :", e)
        speak("Something went wrong")
        return None


# -------------------- DESTINATION EXTRACTION --------------------

def extract_destination(user_text):

    patterns = [
        r'chennai\s+to\s+([\w\s]+)',
        r'bus\s+to\s+([\w\s]+)',
        r'go\s+to\s+([\w\s]+)',
        r'travel\s+to\s+([\w\s]+)'
    ]

    for pattern in patterns:

        match = re.search(pattern, user_text)

        if match:
            destination = match.group(1).strip()
            return destination

    return None


# -------------------- FETCH NEXT BUS --------------------

def fetch_next_bus(destination):

    current_time = datetime.now().time()

    query = """
    SELECT departure_time, fare
    FROM transport_det
    WHERE LOWER(source) = 'chennai'
    AND LOWER(destination) = %s
    AND LOWER(transport_type) = 'bus'
    ORDER BY departure_time
    """

    cursor.execute(query, (destination.lower(),))

    buses = cursor.fetchall()

    # No buses found
    if not buses:
        return None, None

    # Check buses for today
    for dep_time, fare in buses:

        if dep_time >= current_time:
            return dep_time.strftime("%H:%M"), fare

    # If all buses departed, show first bus tomorrow
    first_bus_time, fare = buses[0]

    return first_bus_time.strftime("%H:%M"), fare


# -------------------- MAIN PROGRAM --------------------

def main():

    user_text = take_voice_input()

    if not user_text:
        speak("Please try again")
        return

    destination = extract_destination(user_text)

    if not destination:
        speak("Please say in format Chennai to Vellore")
        return

    print("Destination :", destination)

    departure_time, fare = fetch_next_bus(destination)

    if departure_time:

        result = (
            f"The next bus from Chennai to "
            f"{destination} departs at "
            f"{departure_time} and costs "
            f"rupees {fare}"
        )

        speak(result)

    else:

        speak(
            f"Sorry, no buses available from Chennai to {destination}"
        )

    db.close()


# -------------------- RUN APPLICATION --------------------

if __name__ == "__main__":
    main()
