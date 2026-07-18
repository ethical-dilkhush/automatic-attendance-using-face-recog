# automatic-attendance-using-face-recog

Automatic attendance system using face recognition.  
This project uses OpenCV and LBPH face recognition to mark attendance from a live camera feed and stores records in CSV.

## Features

- Face detection and recognition with OpenCV Haar cascades and LBPH
- Train dataset from locally captured face samples
- Student details management with local MySQL database
- Attendance export to CSV

## Prerequisites

- Python 3.8+
- Tkinter
- MySQL Server
- Webcam
- Required Python packages: `opencv-python`, `pillow`, `numpy`, `mysql-connector-python`

## Setup

```bash
pip install -r requirements.txt
```

## Database setup

Create MySQL database and student table typically used by this project before launching the app:

```sql
CREATE DATABASE IF NOT EXISTS face_recognizer;
USE face_recognizer;
CREATE TABLE student (
  Student_id INT PRIMARY KEY,
  Name VARCHAR(100),
  Dep VARCHAR(100),
  Course VARCHAR(100),
  Year VARCHAR(50),
  Semester VARCHAR(50),
  Gender VARCHAR(20),
  DOB VARCHAR(20),
  Email VARCHAR(100),
  Phone VARCHAR(20),
  Address VARCHAR(200),
  Roll VARCHAR(50),
  Teacher VARCHAR(100),
  PhotoSample VARCHAR(10)
);
```

## Usage

1. Start `main.py`.
2. Use **Student Details** to add records.
3. Use **Train Data** to train classifier from `data/`.
4. Use **Face Detector** to start recognition and mark attendance.
5. Attendance is saved to `Dilkhush.csv`.

## Notes

- Some image paths in source are Windows-specific local paths, so running on Windows/mapped drives is expected.
- Samples are stored under `data/` as numbered face captures.
- Generated artifacts: `classifier.xml` and `Dilkhush.csv`.
