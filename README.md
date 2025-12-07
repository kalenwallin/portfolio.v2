<p align="center">
  <a href="https://v2.kalenwallin.com/">
    <img src="https://kalenwallin.com/_next/image?url=https%3A%2F%2Fwww.notion.so%2Fimage%2Fhttps%253A%252F%252Fi.kalenwallin.com%252Ffile%252Fportfoliov2%252Fmedia%252Ffavicon.svg%3Ftable%3Dblock%26id%3Dbff8ee6e-b3bf-4a01-9de9-79d3b96fe26f%26cache%3Dv2&w=1080&q=75" height="96">
    <h3 align="center">Portfolio.v2</h3>
  </a>
</p>

<p align="center">A Django website to showcase my skills through experiences.</p>

# Demo

https://github.com/kalenwallin/portfolio.v2/assets/31481852/80ee7028-6090-472f-8ddb-4239c1e2a695

[Visit this website](https://v2.kalenwallin.com/) or [learn more about this project on my blog](https://kalenwallin.com/portfoliov2).

## Getting Started

### Installation

1. Create a virtual environment
2. Activate the virtual environment
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Get environment variables from Vercel

   ```bash
   vc env pull
   ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

The server will start at `http://127.0.0.1:8000/`

### Optional Commands

- Create a superuser to access the admin panel:

  ```bash
  python manage.py createsuperuser
  ```

- Collect static files (for production):

  ```bash
  python manage.py collectstatic
  ```
