# Workday

## Description
This repository is for handling Workday data ingestion and processing in the UBC Live team. 

## Data format (JSON)
All course data is now structured as JSON conforming to the schema defined in `schema_definition.json`. This schema serves as the authoritative reference for data structure, validation, and integration requirements.
### Purpose of the Schema
The JSON schema defines the structure and validation rules for Workday course data. It ensures data consistency, type safety, and proper formatting across all ingestion and processing pipelines. The schema is based on JSON Schema Draft 2019-09 specification.
### Schema fields
**course**  
Official title of the course as shown in workday, with section.
**Type:** string
```json
"DSCI_V 100-003"
```
**instructor**  
Primary instructor responsible for teaching the section.
**Type:** string
```json
"Katherine Burak"
```
**section_type**  
Type of instructional delivery for the section.
**Type:** string
```json
"Lecture"
"Lab"
"Tutorial"
"Discussion"
```
**delivery_format**  
How the course is delivered.
**Type:** string
```json
"In-Person"
"Online"
"Hybrid"
"Remote"
```
**registered_students**  
Current number of enrolled students in the section.
**Type:** number
```json
120
```
**waitlisted_students**  
Number of students on the waitlist for the section.
**Type:** number
```json
15
```
**class_time**  
Start and end time of the scheduled class session in 24-hour format.
**Type:** string
```json
"15:30-17:00"
"08:30-10:00"
```

**days_of_week**  
Days on which the class meets, stored as a delimiter-separated list in order of the week.
**Type:** string
```json
"Mon|Wed|Fri"
"Tue|Thu"
```
### Example

```json
{
  "course": "DSCI_V 100-003",
  "instructor": "Katherine Burak",
  "section_type": "Lecture",
  "delivery_format": "In-Person",
  "registered_students": 162,
  "waitlisted_students": 0,
  "class_time": "15:30-17:00",
  "days_of_week": "TueThu"
}
```

- Raw data will be in `data/raw/` and cleaned data in `data/raw/clean/`.
- Raw data is in the form of a raw html file, as it is sourced from a workday page.
- Processed data must conform to the data defined in `schema_definition.json`.
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
## Project Workflow
### Data fetch mechanics
- The data is webscraped unconventionally with Selenium and some manual authentication.
- Produces a single static HTML file.
### Data Parser
- Extracts structured course information from the raw HTML file.
### Schema Validation
- All parser output must match the schema defined in `schema_definition.json`.


