# Design Thinking and IBM Loop Report

## 1. Introduction

Design thinking helps develop products by understanding users, defining problems, exploring ideas, creating prototypes, and testing proposed solutions.

The Library Management Platform applies this approach to improve library operations for students, librarians, faculty, and administrators.

## 2. Empathize

### Users and Their Needs

- Students and faculty need to search for books and check availability.
- Librarians need to manage book records, borrowing, and returns.
- Administrators need reliable records and operational reports.

### Observed Challenges

- Manual records can be difficult to maintain.
- Book availability may be difficult to track.
- Borrowing and return records can become inconsistent.
- Overdue items and fines may require manual follow-up.

These are initial problem assumptions that should be validated with real users.

## 3. Define

**Problem statement:** Library users and staff need a centralized and reliable way to manage book information and borrowing activities so that routine library operations become easier to track and maintain.

## 4. Ideate

Potential solutions include:

- A searchable book catalog.
- User authentication and role-based access.
- Book issue and return tracking.
- Automated overdue fine calculation.
- Notifications for due dates and overdue books.
- Reports for library administrators.

## 5. Prototype

The current prototype is a basic Java application built with Maven and packaged in Docker. Product requirements and the proposed architecture are documented in this repository.

The prototype does not yet implement the complete library workflow or database integration.

## 6. Test

The current Java application has been run in a Docker container, and its welcome messages were observed successfully.

Future usability and functional testing should involve representative users and cover:

- Searching for books.
- Checking availability.
- Issuing and returning books.
- Calculating overdue fines.
- Access permissions and data validation.

No user research or usability study is claimed to have been completed.

## 7. IBM Design Thinking Principles

### Focus on User Outcomes
Prioritize improvements that help users complete library tasks accurately and efficiently.

### Restless Reinvention
Review feedback and improve the product iteratively rather than assuming the first design is final.

### Diverse Empowered Teams
Include students, librarians, administrators, and technical team members in product decisions.

## 8. IBM Loop

The IBM Loop supports continuous learning through three activities:

- **Observe:** Understand user behavior, needs, and difficulties.
- **Reflect:** Analyze findings, identify gaps, and revise assumptions.
- **Make:** Build or improve a prototype and test it with users.

Repeat the loop as new feedback and evidence become available.

## 9. Conclusion

Design thinking and the IBM Loop provide a structured approach for developing a user-focused Library Management Platform. The next stage is to validate assumptions with users and implement the core library workflows.
