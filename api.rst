Student:

POST /student/ - add a student
   - student_no
   - first_name
   - middle_name
   - last_name
   - email
   - password
   - course
   - year_level
GET /student/<id> - get a student
PUT /student/<id> - update a student
   - student_no
   - first_name
   - middle_name
   - last_name
   - email
   - password
   - course
   - year_level
   - registration_id
DELETE /student/<id> - delete a student
POST /login
   - student_no
   - password
POST /student/<id>/verify - send verification email
GET /student/<id>/verify - verify student account
   
Subject:

GET /student/<id>/subject/ - get subjects by student id
GET /subject/<id> - get a subject
GET /subject - get list of subjects
GET /subject?student_id=<id> - get list of subjects available for a student
POST /subject/ - create a subject w/o student
   - code
   - description
   - days
   - time_start
   - time_end
   - section
PUT /subject/<id>/register - register a student to a subject
   - student_id

Exam:
   
GET /student/<id>/exam/ - get exams by student id
GET /exam/<id> - get an exam