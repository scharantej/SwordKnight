## Flask Application Design for Character Creation in Pathfinder Roleplaying Game

### HTML Files

- **character_form.html**: This HTML file will provide a form for users to input the details of their character, including their name, ability scores, skills, and equipment.
- **character_sheet.html**: This file will display the details of the character created by the user, including their stats, skills, and equipment.

### Routes

- **@app.route('/character_creation', methods=['GET', 'POST'])**: This route will handle the character creation form. When a user accesses this route, the character_form.html file will be displayed. When a user submits the form, the route will process the input and create a character object.
- **@app.route('/character_sheet/<character_id>)':** This route will display the character sheet for a specific character. The character_id parameter will be used to retrieve the character object from the database. The route will then render the character_sheet.html file with the character details.