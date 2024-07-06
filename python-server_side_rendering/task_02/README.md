## 2. Creating a Dynamic Template with Loops and Conditions in Flask
In this task, you will enhance your Flask application by integrating dynamic content into your HTML templates using Jinja’s loop and conditional constructs. You will read a list of items from a JSON file and display them dynamically on a web page.

### Objective
- Use Jinja’s loop and conditional constructs to dynamically render content in HTML templates.
- Read and parse JSON data in Python.
- Integrate dynamic content into your Flask application.

### Instructions
1. Prepare Your Flask Application:
- Continue using the Flask application you created in the previous exercises.
- Ensure you have a basic understanding of Jinja’s templating syntax.


2. Create a Dynamic Template:
- In your `template`s folder, create a new HTML template named `items.html.`
- This template should include a loop to iterate over a list of items and display each item.
- Items must be displayed as an unordered list.
- Add a conditional statement to display a message “No items found” if the list is empty.

3. Define the Data for the Template:
- In your project directory, create a file named `items.json.`
- Populate `items.json` with a list of items. Example: `json { "items": ["Python Book", "Flask Mug", "Jinja Sticker"] }`
- Experiment with different lists, including an empty list, to see how your template responds.

4. Add a Route in Flask:

- Create a new route in your Flask application to render the `items.html` template with the list of items.
- Use Python’s `json` module to read the data from `items.json.`
- Pass the list of items to the template for rendering.

### Example Data for Testing:
```
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
```

### Hints:
- Use Python’s `json`module to read data from the JSON file.
- Utilize Jinja’s `{% for %}` loop to iterate over the list of items in the template.
- Use the `{% if %}` statement to conditionally display the message when the list is empty.
- Define the new route in your Flask application and use the `render_template` function to pass the list of items to `items.html.`