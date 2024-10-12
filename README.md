# LAB - Class 29
Project: Cats + Extending User Class 
Author: Maddie Amelia Lewis

## Links and Resources

Template for DjangoX: https://github.com/wsvincent/djangox

## Setup

### .env Requirements

- PORT - Port Number
- DATABASE_URL - URL to the running Postgres instance/db

### How to Initialize/Run Your Application

```manage.py runserver```

### How to Use:

Navigate to the home page to view the application.

### Tests

**How to Run Tests**

Use the following command to run your tests:


`python manage.py test`

**Tests of Note**
Test that the Cat model behaves as expected.
Verify status codes for pages.

**Describe Any Tests That You Did Not Complete**
No tests were skipped; all basic functionalities of cats and news apps were covered. I did not make extensive tests of the whole application.

**Additional Notes**
The project includes a cats app with a Cat model that has the following fields:

- name: A CharField for the cat's name (max length of 100 characters).
- breed: A CharField for the cat's breed (max length of 100 characters).
- nicknames: A CharField for any nicknames (max length of 200 characters, blank allowed).
- emoji_preference: A CharField for the preferred emoji (max length of 20 characters, blank allowed).
- color: A CharField for the cat's color (max length of 50 characters).
- tail: A CharField for tail description (max length of 50 characters).
- age: A PositiveIntegerField for the cat's age.
- magical_properties: A TextField for any magical properties (blank allowed).
- image: An ImageField for the cat's image, with a default value of default_cat.png.
