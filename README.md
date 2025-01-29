# blood-bank-management-system
1. Introduction
The Blood Bank Management System (BBMS) is a database management system designed to manage the storage, donation, and distribution of blood. It provides an efficient way to track blood availability and donor details while ensuring smooth operations within a blood bank.
2. Objectives
•	To maintain records of blood donors and recipients.
•	To manage blood stock effectively.
•	To ensure transparency and traceability of blood donations.
•	To facilitate quick retrieval of blood group information.
3. System Design
The system follows a relational database model, consisting of multiple tables linked through primary and foreign keys. It includes modules for donor registration, blood inventory management, recipient requests, and hospital collaboration.
4. ER Diagram
The Entity-Relationship (ER) diagram represents the relationship between entities such as Donors, Blood Units, Recipients, and Hospitals. The key entities include:
•	Donor: Stores donor details such as name, age, blood group, and contact.
•	Blood Stock: Maintains available blood units with types and expiration dates.
•	Recipient: Contains recipient details and blood request records.
•	Hospital: Tracks hospital details where blood is supplied.
5. Database Tables
The system consists of the following tables:
•	Donor Table: Contains donor ID, name, blood type, contact, and last donation date.
•	Blood Stock Table: Includes blood group, unit count, storage location, and expiry date.
•	Recipient Table: Stores recipient ID, name, blood type needed, and request status.
•	Transaction Table: Maintains records of blood donations and distributions.
6. Implementation
The project is implemented using:
•	Database: MySQL / PostgreSQL
•	Frontend: HTML, CSS, JavaScript
•	Backend: PHP / Python / Java
•	Security: User authentication and access control for data protection.
7. Conclusion
The Blood Bank Management System enhances the efficiency and reliability of blood banks by providing a structured and secure approach to blood donation and distribution. This project ensures timely availability of blood, reduces wastage, and improves overall healthcare services.
