import nltk
import random

greetings = ["hello", "hi", "hey", "good morning", "good evening", "Address", "location", "principal"]
responses = ["Hello!", "Hi there!", "How can I help you?", "Nice to meet you!"]
goodbyes = ["bye", "goodbye", "see you", "see ya", "quit", "exit", "farewell", "take care"]
farewell_responses = [
    "Goodbye! Have a great day!",
    "Thank you for chatting! Come back if you have more questions.",
    "See you later!",
    "Farewell! If you need more information, don't hesitate to ask again.",
    "Have a wonderful day!",
    "It was nice talking to you. Goodbye!"
]

college_info = {
    "name": "Vidya Pratishthans Kamalnayan Bajaj Institute of Engineering and Technology",
    "departments": ["Information Technology", "Computer Engineering", "Mechanical Engineering",
                    "Electrical Engineering", "Civil Engineering", "Artificial Intelligence and Data Science",
                    "Electronics and Telecommunications"],
    "location": "Bhigwan Road, Baramati, Maharashtra - 413133",
    "ranking": "#10 in the SPPU, NAAC Accredited with 'A' Grade",
    "admission_requirements": {
        "UG": "Minimum 50% in 12th standard (PCM) and valid MHT-CET/JEE score",
        "PG": "Bachelor's degree in relevant field with minimum 50% marks"
    },
    "Contact no": "02112-123456, 9876543210",
    "Web site address": "https://vpkbiet.org/",
    "principal": "Dr. R. S. Bichkar",
    "established": 1999,
    "affiliation": "Affiliated to Savitribai Phule Pune University (SPPU) and approved by AICTE",
    "facilities": [
        "Central Library with 50,000+ books",
        "High-tech Computer Labs",
        "Workshops for all engineering branches",
        "Separate hostels for boys and girls",
        "Sports complex with gymnasium",
        "Auditorium with 500 seating capacity"
    ],
    "placement": {
        "average_package": "4.5 LPA",
        "highest_package": "12 LPA (2023)",
        "top_recruiters": ["TCS", "Infosys", "Persistent", "Capgemini", "Accenture"]
    },
    "scholarships": [
        "EBC Scholarship",
        "Government Merit Scholarship",
        "Minority Scholarship",
        "VPK Merit Scholarship"
    ],
    "events": [
        "TechFest - Annual Technical Festival",
        "Cultural Fest - Yuvaan",
        "Sports Week",
        "Alumni Meet"
    ],
    "library": {
        "books": "50,000+ volumes",
        "journals": "200+ national and international",
        "digital": "Access to IEEE, Springer, J-Gate"
    },
    "lab_facilities": [
        "24/7 Internet Connectivity",
        "Cisco Networking Academy",
        "Oracle Academy",
        "Red Hat Academy",
        "Siemens Automation Lab"
    ]
}

def generate_response(user_input):
    tokens = nltk.word_tokenize(user_input.lower())

    if any(token in tokens for token in greetings):
        return random.choice(responses)
    elif any(token in tokens for token in goodbyes):
        return random.choice(farewell_responses)
    elif "name of college" in user_input.lower():
        return f"The name of the college is {college_info['name']} (Established: {college_info['established']})."
    elif "departments" in user_input.lower():
        departments_list = ", ".join(college_info['departments'])
        return f"Departments: {departments_list}"
    elif "location" in user_input.lower() or "address" in user_input.lower():
        return f"The college is located at: {college_info['location']}"
    elif "ranking" in user_input.lower() or "accreditation" in user_input.lower():
        return f"Our college ranking and accreditation: {college_info['ranking']}"
    elif "admission" in user_input.lower() or "requirements" in user_input.lower():
        ug_req = college_info['admission_requirements']['UG']
        pg_req = college_info['admission_requirements']['PG']
        return f"Admission requirements:\nUG Programs: {ug_req}\nPG Programs: {pg_req}"
    elif "principal" in user_input.lower() or "director" in user_input.lower():
        return f"The principal is {college_info['principal']}"
    elif "contact" in user_input.lower() or "phone" in user_input.lower():
        return f"Contact details:\nPhone: {college_info['Contact no']}\nWebsite: {college_info['Web site address']}"
    elif "facilities" in user_input.lower() or "infrastructure" in user_input.lower():
        facilities_list = "\n- ".join(college_info['facilities'])
        return f"College facilities:\n- {facilities_list}"
    elif "placement" in user_input.lower() or "recruiters" in user_input.lower():
        recruiters = ", ".join(college_info['placement']['top_recruiters'])
        return f"Placement details:\nAverage Package: {college_info['placement']['average_package']}\nHighest Package: {college_info['placement']['highest_package']}\nTop Recruiters: {recruiters}"
    elif "scholarship" in user_input.lower() or "financial aid" in user_input.lower():
        scholarships = ", ".join(college_info['scholarships'])
        return f"Available scholarships: {scholarships}"
    elif "events" in user_input.lower() or "fest" in user_input.lower():
        events_list = ", ".join(college_info['events'])
        return f"College events: {events_list}"
    elif "library" in user_input.lower() or "books" in user_input.lower():
        return f"Library resources:\nBooks: {college_info['library']['books']}\nJournals: {college_info['library']['journals']}\nDigital Resources: {college_info['library']['digital']}"
    elif "lab" in user_input.lower() or "laboratory" in user_input.lower():
        labs = ", ".join(college_info['lab_facilities'])
        return f"Laboratory facilities: {labs}"
    elif "established" in user_input.lower() or "year" in user_input.lower():
        return f"The college was established in {college_info['established']}"
    elif "affiliation" in user_input.lower():
        return f"Affiliation: {college_info['affiliation']}"
    else:
        return "I'm sorry, I didn't understand your request. Could you please rephrase your question?"

print("Hello, I'm an engineering college chatbot. How can I help you?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    response = generate_response(user_input)
    print(response)
