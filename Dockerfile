FROM eclipse-temurin:21-jdk

WORKDIR /app

COPY pom.xml .
COPY app/src ./app/src

RUN apt-get update && apt-get install -y maven && mvn clean package && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["java", "-cp", "target/classes", "com.library.App"]
