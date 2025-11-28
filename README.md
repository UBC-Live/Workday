# Workday

## Description
This repository is for handling Workday data ingestion and processing in the UBC Live team. 

## Data format (CSV)
### Header definitions
**course**  
Official title of the course as shown in workday, with section.
```csv
"DSCI_V 100-003"
```
**instructor**  
Primary instructor responsible for teaching the section.
```csv
"Katherine Burak"
```
**section_type**  
Type of instructional delivery for the section.
```csv
"Lecture"
"Lab"
"Tutorial"
"Discussion"
```
**delivery_format**  
How the course is delivered.
```csv
"In-Person"
"Online"
"Hybrid"
"Remote"
```
**registered_students**  
Current number of enrolled students in the section.
```csv
120
```
**waitlisted_students**  
Number of students on the waitlist for the section.
```csv
15
```
**class_time**  
Start and end time of the scheduled class session in 24-hour format.
```csv
"15:30-17:00"
"08:30-10:00"
```

**days_of_week**  
Days on which the class meets, stored as a delimiter-separated list in order of the week.
```csv
"Mon|Wed|Fri"
"Tue|Thu"
```
### Example

```csv
course,instructor,section_type,delivery_format,registered_students,waitlisted_students,class_time,days_of_week
"DSCI_V 100-003","Katherine Burak","Lecture","In-Person",162,0,"15:30-17:00","Tue|Thu"
```

- Raw data will be in `data/raw/` and cleaned data in `data/raw/clean/`.
- Raw data is in the form of a raw html file, as it is sourced from a workday page.
- **Note:** The format of the data or CSV file may change as requirements evolve.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/UBC-Live/Workday.git
   cd Workday
   ```

2. **Create virtual environment** 
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   To deactivate:
   ```bash
   deactivate
   ```

3. **Set up environment variables**

   Copy .env.example contents into a new .env file, then put in API information. **This file is local and should not be pushed, as specified in .gitignore** 

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Data fetch mechanics

The data is webscraped unconventionally with Selenium and some manual authentication. 

