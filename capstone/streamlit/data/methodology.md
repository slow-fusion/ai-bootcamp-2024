## Stages

There are three stages for the web application. 

### Data collection

For the first use case, the data sources (PDFs and text) are manually taken 
from the AI Bootcamp website.

For the Skillsfuture Course Finder, I wrote a script to access the SSG API 
from [SSG Developer site](https://developer.ssg-wsg.gov.sg/webapp/home) to
download the first 500 courses with the keyword "digital". It should be 
noted that this is a subset of the entire course directory; this was 
intentionally done to limit the size of the vector store required later 
for the proof-of-concept. The output is a JSON file with the course details.

### Preprocessing 

With the data sources stored locally, another script was written to parse the 
PDFs, text and JSON (splitting, chunking, turning into embeddings) into 
two separate Chroma vector stores: `aibootcamp_db` and `ssg_courses_db`.

For chunking, I used semantic chunker for PDFs and text, and JSON splitter 
for JSON file.

### Web application 

This part is a standard retreival-augmented generation (RAG) pipeline 
using Langchain. It was repurposed from the code learnt from earlier weeks. 


