# Telemedicine SaaS Portal 🏥

A secure web portal for remote patient-doctor consultations, featuring automated symptom logging, prescription management, and real-time health tracking.

## Description
A secure web portal for remote patient-doctor consultations, featuring automated symptom logging, prescription management, and real-time health tracking via a HIPAA-compliant interface.

## Key Features
- **Patient Dashboard:** Interactive view of vitals history and upcoming appointments.
- **Symptom Tracker:** Data-driven logging system for chronic condition monitoring.
- **Secure Messaging:** Encrypted communication channel between clinicians and patients.

## Tech Stack
- **Language:** Python
- **Libraries:** Streamlit, Pandas, SQLite, Plotly
- **Security:** SHA-256 password hashing and session-based access control.

## Engineering Logic
- **Backend:** The portal utilizes a relational database to maintain patient records and a secure session manager to prevent unauthorized data access.
- **Software Engine:** A Streamlit interface provides a "Clinic View" for doctors to see a prioritized list of patients based on reported symptom severity scores.
