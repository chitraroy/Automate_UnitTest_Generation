# Project COMP 264: Cloud Machine Learning
## Introduction
Throughout this project assignment, each team needs to construct “A full stack serverless
intelligent enabled application” using cloud Artificial Intelligence (AI) services i.e ready
available pre-trained AI APIs’.
The application should help address a real-world business problem. This could be a simple
translation service for a news entity, or an intelligent recommender based on extracted
information or a simple chatbot to address a certain service.
Over the course of weeks 3-6 we covered 2 full stack projects using Chalice AI framework and
amazon AI services.
Durring the project each team will brainstorm, research, design, build and test a serverless
web-based AI application.
The project would be governed by a set of deliverables and there are certain check points with
the professor, as illustrated in the project timetable key-milestones section.
Deliverables will be evaluated based on the rubric illustrated in the Rubric section. Grading is
both at the team level and at the individual level.
A project plan should be built by the team and updated on a weekly basis, in addition, a simple
log of all team meetings should be maintained. Both should be submitted with final project
documentation and code as appendices to the project report.
At the end of the project, the team needs to present their work to the class, as per the time
table.
Technology stack to be used for the project:
1. Programming language backend: Python
2. Programming language frontend: Any frontend framework that supports RESTful
architecture.
3. Data storage: aws S3 or DynamoDB or both as needed.
4. Software development toolkit: aws Boto3
5. Serverless framework: aws chalice
6. Testing: local host
7. Operating system: Linux
8. AI services:
9. Minimum two aws AI services such as: recognition, polly , comprehend, Lex ..etc
10. Aws IAM
11. Architecture: RESTful api , function as a service (FaaS)
pg. 1 COMP 264 Project Prepared by: Professor Mayy Habayeb
Data sets
Each team will identify if any external datasets are required for the project, these might be
required for look-ups and testings purposes such as image documents or image road signs but
not not for training purposes.
Deliverables:
1. Rational for the project: Explain the idea, benefits for end user and a short feasabilty
including estimated operating (running cost).
2. Scope: Clear scope document illustrating which fuctionalities will be delivered.
3. Research requirements:
a. Provide a summary of options in the market for AI enabled services similar to
your suggested service.
b. Provide a literature review of at least one published papper in the domain.
4. Service general requirements:
a. Secuirty of any sensitive information such as user ids , passwords..etc needs to
be addressed according to best practices.
b. Logs and audit logs, as needed.
c. Address Multi-user scenarios, if needed.
d. User friendly : Easy for user to understand and navigate.
5. Design document:
a. List of use cases or user stories (limit it to two to four)
b. List of functional requirements.( These are based on point a above)
c. Design graphs illustrating:
i. Architecture of the solution. This should make clear all the endpoints and
the AI stack layers (you can use Microsoft Visio)
ii. Interaction diagram illustrating the interactions between the various
components of the solution, please choose clear, representive names for
each components. (you can use Visio)
d. List of design decisions and an explanation for each.
e. User interface mockup (you can use wire or any other software)
The design should take into consideration the software design principles “ Separation of
concerns” and “single responsibility”. In addition, to eliminating as much as possible, the
dependency on the cloud vendor, for future portability of the application to a different cloud
vendor.
6. Code:
a. Front end code
b. Orchestration layer code
c. Backend code
Code should be documented and especial attention to handle exception cases.