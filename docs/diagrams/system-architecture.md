# Library Management Platform — System Architecture

```mermaid
flowchart TD
    U[Students and Faculty]
    L[Librarian]
    A[Administrator]

    UI[User Interface]
    AUTH[Authentication and Authorization]
    APP[Library Application Services]
    BOOKS[Book Catalog and Search]
    CIRC[Issue and Return]
    FINES[Fine Calculation and Notifications]
    DB[(Database - Planned)]
    DEVOPS[GitHub and Maven]
    DOCKER[Docker Container]
    MON[Monitoring - Planned]

    U --> UI
    L --> UI
    A --> UI
    UI --> AUTH
    AUTH --> APP
    APP --> BOOKS
    APP --> CIRC
    APP --> FINES
    BOOKS --> DB
    CIRC --> DB
    FINES --> DB
    DEVOPS --> DOCKER
    DOCKER -. logs and metrics .-> MON
```

## Notes

- The Java demo application runs successfully inside Docker.
- Database integration and the full user interface are planned work.
- Monitoring and additional infrastructure are planned for later phases.
