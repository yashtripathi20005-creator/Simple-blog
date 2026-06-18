from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts data
posts = [
    {
        'id': 1,
        'title': 'Getting Started with Python',
        'date': 'January 15, 2026',
        'author': 'John Doe',
        'excerpt': 'Python is a versatile programming language that is great for beginners...',
        'content': 'Python is a versatile programming language that is great for beginners and experts alike. It has a simple syntax that mimics natural language, making it easy to read and understand. In this post, we\'ll cover the basics of Python programming and how to set up your development environment.',
        'tags': ['Python', 'Programming', 'Beginners']
    },
    {
        'id': 2,
        'title': 'Web Development with Flask',
        'date': 'January 12, 2026',
        'author': 'Jane Smith',
        'excerpt': 'Flask is a lightweight WSGI web application framework...',
        'content': 'Flask is a lightweight WSGI web application framework designed to make getting started quick and easy, with the ability to scale up to complex applications. It\'s micro-framework that doesn\'t require particular tools or libraries, making it perfect for small to medium projects.',
        'tags': ['Flask', 'Web Development', 'Python']
    },
    {
        'id': 3,
        'title': 'CSS Grid vs Flexbox',
        'date': 'January 10, 2026',
        'author': 'Mike Johnson',
        'excerpt': 'Both CSS Grid and Flexbox are powerful layout systems...',
        'content': 'Both CSS Grid and Flexbox are powerful layout systems that serve different purposes. Flexbox is best for one-dimensional layouts (rows or columns), while Grid is perfect for two-dimensional layouts (both rows and columns). Understanding when to use each will make you a better front-end developer.',
        'tags': ['CSS', 'Layout', 'Web Design']
    },
    {
        'id': 4,
        'title': 'JavaScript Async/Await Explained',
        'date': 'January 8, 2026',
        'author': 'Sarah Wilson',
        'excerpt': 'Async/await makes asynchronous JavaScript code look and behave like synchronous code...',
        'content': 'Async/await is a modern way to handle asynchronous operations in JavaScript. It makes your code look cleaner and more readable by removing the need for chaining .then() methods. In this tutorial, we\'ll explore how to use async/await effectively in your projects.',
        'tags': ['JavaScript', 'Async', 'Programming']
    },
    {
        'id': 5,
        'title': 'Database Design Best Practices',
        'date': 'January 5, 2026',
        'author': 'David Chen',
        'excerpt': 'Good database design is crucial for application performance...',
        'content': 'Good database design is crucial for application performance and maintainability. This post covers normalization, indexing strategies, and common pitfalls to avoid. We\'ll also discuss different database types and when to use each one.',
        'tags': ['Database', 'SQL', 'Architecture']
    },
    {
        'id': 6,
        'title': 'Introduction to DevOps',
        'date': 'January 3, 2026',
        'author': 'Emily Brown',
        'excerpt': 'DevOps bridges the gap between development and operations teams...',
        'content': 'DevOps bridges the gap between development and operations teams, promoting collaboration and automation throughout the software development lifecycle. Learn about the core principles of DevOps and how to implement them in your organization.',
        'tags': ['DevOps', 'CI/CD', 'Automation']
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
