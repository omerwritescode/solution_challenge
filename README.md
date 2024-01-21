# solution_challenge
Solution - Making a Job Matching Platform
Topic - Decent Work and Economic Growth

This repository contains 1 Main Python file and 2 HTML files

Python File:
This file defines a flask web application with 2 routes: one for displaying job listings on the home page and another for handling job matching based on user-submitted skills. The job matching algorithm checks for matches in skills between the user and the available jobs, and the results are then displayed to the user. This script serves as the backend logic for the job matching platform.

HTML files:
The templates.html file is the template for the home page, providing a form for users to input their skills and displaying a list of available jobs.
The match_result.html file is the template for displaying the results of the job matching process, showing the user's entered skills and a list of matched jobs or a message if no matches were found. The templates use Jinja templating to dynamically insert data from the Flask application into the HTML structure.
