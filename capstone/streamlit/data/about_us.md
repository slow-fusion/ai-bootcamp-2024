A detailed page outlining the project scope, objectives, data sources, and features.

## Project Scope

Domain area: Understanding and Finding Courses

1. Course Structure Explainer

    - This use case is to build an means to allow user to ask questions
    regarding the AI bootcamp course. The belief is that there are still 
    many people who prefer to receive the information by asking questions, 
    instead of reading the PDF that is already posted on the Canvas site.
    This belief is supported by the questions posted on the discussion 
    forums, even though the answers are usually already given within the 
    PDF info deck, or the FAQ page.

    - Users can ask and get answers on how long the duration will be, 
    what is the passing criteria for the course, so that they may make a 
    decision on whether to commit to the course or not. Note that this is 
    *not* meant to answer questions on course content, such as limitations of 
    AI, the reasons why AI can halluciate, or why building a RAG is usually
    better than re-training a large language model.

2. Prompt to search for courses from Skillsfuture 

    - This use case aims to build a prompt to allow users to use natural 
    language to search for Skillsfuture courses. While there is an existing
    website to search for such courses, it is a 'structured search', by 
    specifying course type, training provider, course fees, and keywords. 
    This course finder will allow users to use unstructured natural language
    to search courses, which is powered by a large language model under the
    hood, assisted by retrieval-augmented generation.


## Data Sources

The following will be the data sources for the use cases.

1. Course Structure Explainer

    - [Info Deck on AI Bootcamp](https://d17lzt44idt8rf.cloudfront.net/aicamp/shared/AI%20Champion%20Bootcamp%20-%20Pilot%2002%20-%20Info%20Deck.pdf) from the Canvas Learning Management System. 

    - [FAQ](https://canvas.instructure.com/courses/9748108/pages/faqs?module_item_id=112615241) page from the Canvas Learning Management System.

    - "Info Deck on Project Phase" from the Canvas Learning Management System. 

2. Skillsfuture Course Finder to search for courses from Skillsfuture 

    - Skillsfuture course directory
    Skillsfuture SG (SSG) provides a number of APIs to allow developers 
    to interact with them. One of these APIs allow access to SSG's course 
    information. Through the API, I downloaded a list of the first 500 
    digital courses to be used as the data source for searching SSG courses.









