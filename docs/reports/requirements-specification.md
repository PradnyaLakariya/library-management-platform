# Library Management Platform
## Functional and Non-Functional Requirements Specification

### 1. Functional Requirements

#### FR-01: User Authentication
The platform should support secure login and role-based access for
administrators, librarians, students, and faculty members.

#### FR-02: Book Catalog Management
Authorized users should be able to add, view, update, and remove
book records, including title, author, category, ISBN, and shelf location.

#### FR-03: Book Search and Availability
Users should be able to search the catalog and view book availability.

#### FR-04: Book Issue and Return
The platform should record book borrowing and returns and maintain
accurate inventory quantities.

#### FR-05: Fine Calculation
The platform should calculate overdue fines according to configured
rules and applicable user categories.

#### FR-06: Notifications
The platform should support reminders for upcoming due dates and
notifications for overdue books.

#### FR-07: Administrative Reporting
Authorized administrators should be able to review inventory,
borrowing, returns, and overdue-book summaries.

### 2. Non-Functional Requirements

#### NFR-01: Security
Passwords must be stored using a suitable password-hashing algorithm.
Access must be restricted according to user roles, and network
communication should use HTTPS in a deployed environment.

#### NFR-02: Performance
The design target is for book-search API responses to complete
within 500 milliseconds under the specified test workload.

#### NFR-03: Availability and Scalability
The architecture should support reliable deployment and future
horizontal scaling as user demand increases.

#### NFR-04: Maintainability
The codebase should use a clear directory structure, modular
components, version control, and documented build instructions.

#### NFR-05: Data Integrity
Book inventory, user records, and borrowing transactions should
remain consistent when books are issued or returned.

### 3. Validation

Functional requirements should be validated through feature tests.
Performance, security, and availability targets require appropriate
testing before they can be considered achieved.

### 4. Current Implementation Status

The current project includes a basic Java application built with
Maven and successfully executed in Docker. The requirements above
describe the intended platform and are not all implemented yet.
