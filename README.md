# Library Management Platform

## 1. Project Overview

The Library Management Platform aims to simplify library operations by providing a centralized system for managing books, borrowing, returns, and fines.

This project is being developed as part of Unit 1: Product Engineering and Design Thinking.

## 2. Business Problem

Traditional library processes may rely on manual records, making it difficult to track book availability, borrowing history, returns, and overdue fines efficiently.

The proposed platform aims to improve accuracy, accessibility, and operational efficiency.

## 3. Project Objectives

- Organize library book information.
- Support book searching and availability tracking.
- Plan borrowing and return management.
- Define overdue fine calculation requirements.
- Establish a foundation for future automation and monitoring.

## 4. Technology Stack

- Java 21
- Apache Maven
- Docker
- Git and GitHub
- Ubuntu on AWS EC2

## 5. Current Implementation

- Java application created.
- Maven project configured.
- Application packaged and tested in Docker.
- Product engineering documentation added.
- System architecture documented.

Database integration, a complete user interface, and advanced library features remain planned work.

## 6. Repository Structure

- `app/` — Java application source code and related folders.
- `docs/reports/` — Product vision, requirements, business justification, stakeholder analysis, design thinking, and roadmap documents.
- `docs/diagrams/` — System architecture documentation.
- `Dockerfile` — Docker image build instructions.
- `pom.xml` — Maven project configuration.

## 7. Run the Application

Build the application with Maven:

```bash
mvn clean package
```

Run the Java application:

```bash
java -cp target/classes com.library.App
```

Build the Docker image:

```bash
sudo docker build -t library-management-platform:1.0 .
```

Run the Docker container:

```bash
sudo docker run --rm library-management-platform:1.0
```

## 8. Documentation

Refer to `docs/reports/` for the business justification, product vision, requirements specifications, stakeholder and persona analysis, design thinking report, and engineering roadmap.

## 9. Future Enhancements

- Database integration
- User authentication and role-based access
- Book catalog and search interface
- Borrowing and return workflows
- Fine management and notifications
- Automated delivery and monitoring

## 10. Repository

GitHub: https://github.com/PradnyaLakariya/library-management-platform
