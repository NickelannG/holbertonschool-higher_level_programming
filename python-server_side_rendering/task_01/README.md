## 1. Creating a Basic HTML Template in Flask
In this task, you will build a basic Flask application that serves a web page using a Jinja template. You will create a simple HTML template that includes various elements like headings, paragraphs, and lists, and learn how to render it as a web page using Flask. Additionally, you will learn to create reusable templates for headers and footers to promote code reusability and consistency across multiple pages.

### Objective
- Set up a Flask environment and create a basic Flask application.
- Design HTML templates using Jinja for dynamic content rendering.
- Implement reusable components in templates to maintain consistent layout across pages.

### Instructions
1. Set Up Your Flask Environment:

- Ensure Python is installed on your system.
- Install Flask using pip: sh pip install Flask

2. Create a Basic Flask Application:

- In your project directory, create a Python file named `task_01_jinja.py`.
- Write a basic Flask application with a route that renders an HTML template.

### Example:
```
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html')

   if __name__ == '__main__':
       app.run(debug=True, port=5000)
```

1. Design Your HTML Template:
In a `templates` folder within your project directory, create an HTML file named `index.html.`
Design a simple HTML page with a heading (`<h1>`), a paragraph (`<p>`), and an unordered list (`<ul>` with `<li>` items).

### Example content for index.html:
```
   <!doctype html>
   <html lang="en">
   <head>
       <title>My Flask App</title>
   </head>
   <body>
       <h1>Welcome to My Flask App</h1>
       <p>This is a simple Flask application.</p>
       <ul>
           <li>Flask</li>
           <li>HTML</li>
           <li>Templates</li>
       </ul>
   </body>
   </html>
```

1. Render the Template in Flask:

- Use Flask’s `render_template` function to render the HTML template when the corresponding route is accessed.

2. Create Reusable Header and Footer Templates:

- In the `templates` folder, create two new HTML files: `header.html` and `footer.html`.
- Design simple but distinct layouts for the header and footer.

### Example content for header.html:
```
   <header>
       <h1>My Flask App</h1>
   </header>
```

Example content for `footer.html:` `html <footer> <p>&copy; 2024 My Flask App</p> </footer>`

1. Design Multiple Pages with Shared Header and Footer:

- Create additional HTML pages for different content such as `about.html` and `contact.html.`
- In each of these pages, include the header and footer templates without duplicating their code.

2. Modify Flask Routes:
- Add new routes in your Flask application corresponding to the additional pages you created.

### Example:
```
   @app.route('/about')
   def about():
       return render_template('about.html')

   @app.route('/contact')
   def contact():
       return render_template('contact.html')
```

### Hints:
- Ensure your Flask application runs on port 5000.
- Use the render_template function from Flask to render HTML templates.
- Utilize Jinja’s {% include %} statement to include reusable components like headers and footers.
