# AI-DRIVEN-VOISE-BASED-TRANSPORT-ENQUIREY-SYSTEM
AI-powered voice-based public transport enquiry assistant using Python, Speech Recognition, NLP, and MySQL for real-time bus schedule retrieval.

The system accepts speech input, processes transport requests using NLP techniques, retrieves transport schedules from a MySQL database, and responds with both text and voice output.

---

## Features

- Voice-based transport enquiry
- Speech-to-text using Google Speech Recognition
- Text-to-speech response system
- MySQL database integration
- Automatic destination extraction using Regex
- Real-time next-bus lookup
- Error handling for unclear speech and connectivity issues
- AI-driven conversational interaction

---

## Technologies Used

### Programming Language
- Python

### Libraries
- speech_recognition
- pyttsx3
- mysql-connector-python
- re
- datetime

### Database
- MySQL

---

## System Workflow

1. User speaks:
   "Chennai to Vellore"

2. System converts speech to text

3. Destination city is extracted

4. Database is queried for next available bus

5. System responds with:
   departure time and fare

6. Voice output is generated

---

## Database Structure

| Field | Description |
|---|---|
| source | Departure city |
| destination | Arrival city |
| departure_time | Bus departure time |
| fare | Ticket fare |
| transport_type | Type of transport |

---

## Sample Voice Output

"The next bus from Chennai to Vellore departs at 08:30 and costs rupees 260"

---

## Future Enhancements

- Multi-language support
- Train and metro integration
- Live GPS tracking
- Mobile app integration
- AI chatbot support
- Offline speech recognition
- GUI dashboard

---

## Developed By

Suganthi Jeba Priya
ECE Student
