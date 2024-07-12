# AI-POWERED BOOK MANAGEMENT AND RECOMMENDATIONS 
## USING OPEN SOURCE TECHNOLOGIES WITH GOOGLE WORD2VEC INTEGRATION

Download the model [here](https://drive.google.com/file/d/1eqFnBD_KstlCuouskJgHGhRNyW33LeKT/view?usp=sharing).

### Introduction
- Developed a Django-based web application for book management and recommendations.
- Integrated advanced AI techniques for personalized book recommendations and interactive data visualization.

### Problem Statement
- Aimed to enhance book discovery and management efficiency.
- Addressed issues with traditional book management systems lacking robust recommendation engines and interactive data visualization.

### Main Objectives
- Implement CRUD Operations: Enable Create, Read, Update, and Delete functionalities for books with comprehensive metadata.
- AI-Powered Recommendations: Use AI models to suggest books based on user input and browsing history.
- Interactive Data Visualization: Utilize Plotly for visualizing trends in book categories over publication years.

### Methodology
- Backend Framework: Django with SQLite database.
- Frontend Development: HTML templates rendered by Django, Bootstrap for responsive design.
- AI Integration: Word embeddings using Google Word2Vec models for semantic analysis and cosine similarity for recommending similar books.
- Data Visualization: Plotly library for creating interactive graphs showcasing book trends.

### Technologies Used
- Framework: Django
- Database: SQLite
- AI Tools: Numpy, smart_open (for word embeddings), PyMuPDF (for PDF metadata extraction)
- Data Visualization: Plotly

### Importance of Project
- Enhanced User Experience: Provides personalized book recommendations tailored to individual preferences.
- Research Advancement: Contributes to AI-driven recommendation systems and data visualization research applied to book datasets.
- Educational Impact: Demonstrates practical applications of AI and data science techniques in real-world scenarios.

### Future Plans
- Scalability: Scale the application to handle larger datasets and improve performance.
- API Integration: Incorporate external APIs for real-time updates on book availability and pricing.
- Continuous Improvement: Gather user feedback to enhance features and usability based on user needs.

- **Models:** Defined a Book model with various fields including file uploads (`FileField`), image uploads (`ImageField`), and statistical data (`IntegerField`, `CharField`, `DateTimeField`).

- **Views:** Implemented views for searching books (`search_books`), displaying book details (`book_detail`), showing book statistics (`book_stats`), and an about page (`about`).

- **Admin Configuration:** Customized the Django admin interface for the Book model using `ImportExportModelAdmin` for data import/export capabilities.

- **Resources:** Created a resource class (`BookResource`) for importing and exporting data related to the Book model using `import_export`.

- **Utils:** Developed utility functions (`load_word2vec_model`, `get_embedding`, `find_similar_books`) for text processing and finding similar books based on embeddings.

- **Templates:** Created HTML templates (`home.html`, `book_detail.html`, `trend.html`) using Django template language for rendering search results, book details, and trend graphs.

- **Styling:** Applied CSS styles to enhance the frontend interface, including responsive design and visual enhancements.

- **URL Routing:** Configured URL patterns (`urls.py`) to route requests to appropriate views for search, book details, trends, and about pages.

- **Graph Visualization:** Integrated Plotly for generating and displaying stacked bar charts (`trend.html`) visualizing book categories by publication year.

- **Deployment:** Prepared `INSTALLED_APPS` configuration for Django settings, including necessary packages (`jazzmin`, `import_export`) for functionality and styling.

These project notes cover essential aspects from introduction to future plans, outlining objectives, methodology, technologies used, and future directions.





![Untitled 8](https://github.com/user-attachments/assets/34d2d148-c48e-4dcf-9d2a-17ca39ccab18)
![Untitled 7](https://github.com/user-attachments/assets/85808633-6ae3-4e5c-81c4-f4129525e935)
![Untitled 6](https://github.com/user-attachments/assets/a35ac119-d6ff-47ab-9e00-b6afb9f8d236)
![Untitled 5](https://github.com/user-attachments/assets/0b2ce69c-1271-4b03-8474-e51b0c171338)
![Untitled 9](https://github.com/user-attachments/assets/9bab035e-6c67-4fae-a5c0-aad5fc521232)
![Untitled 10](https://github.com/user-attachments/assets/a8f9f255-e655-420d-880b-f397f5c9c2c6)
![3](https://github.com/user-attachments/assets/09f60d4d-1149-49d2-91f5-913faf11b846)
![Untitled 4](https://github.com/user-attachments/assets/0269462f-5c24-4051-a1cf-81682e7d76c2)
![2](https://github.com/user-attachments/assets/a413ab1c-ab0f-467c-8379-9388a071d2a1)
![1](https://github.com/user-attachments/assets/49023df3-7062-4047-9f78-9e9bebf7e00f)
![9](https://github.com/user-attachments/assets/39126b98-c652-4dc1-b24c-08ffc107e68c)
![4](https://github.com/user-attachments/assets/f07dd0d3-1453-42b6-87f5-9ffcb988e531)

**My Contacts**

**WhatsApp**  
+255675839840  
+255656848274

**YouTube**  
[Visit my YouTube Channel](https://www.youtube.com/channel/UCjepDdFYKzVHFiOhsiVVffQ)

**Telegram**  
+255656848274  
+255738144353

**PlayStore**  
[Visit my PlayStore Developer Page](https://play.google.com/store/apps/dev?id=7334720987169992827&hl=en_US&pli=1)

**GitHub**  
[Visit my GitHub](https://github.com/shamiraty/)

