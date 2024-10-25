# Streamlit web application

This part contains the code for the Streamlit web application. 

## Related Docker commands

To build the Docker image locally for testing, use the following command.

    docker build -t abc2024-query .

To run the Docker image locally for testing, use the following command.

    docker run -e OPENAI_API_KEY=<API_key> -e MAIN_PASSWORD=<password> -p 8501:8501 abc2024-query

To build the docker image and push it into DockerHub, use the following 
command.

    docker buildx build --push --platform linux/amd64 -t slowfusion/abc2024-query .
