
# Import necessary modules
from flask import Flask, request, render_template

# Create a Flask application
app = Flask(__name__)

# Define the character creation route
@app.route('/character_creation', methods=['GET', 'POST'])
def character_creation():
    if request.method == 'GET':
        # Display the character creation form
        return render_template('character_form.html')
    else:
        # Process the form submission and create a character object
        name = request.form['name']
        race = request.form['race']
        class_ = request.form['class_']
        alignment = request.form['alignment']
        ability_scores = {
            'strength': request.form['strength'],
            'dexterity': request.form['dexterity'],
            'constitution': request.form['constitution'],
            'intelligence': request.form['intelligence'],
            'wisdom': request.form['wisdom'],
            'charisma': request.form['charisma']
        }
        skills = {
            'athletics': request.form['athletics'],
            'intimidation': request.form['intimidation'],
            'perception': request.form['perception']
        }
        equipment = [
            request.form['weapon'],
            request.form['armor'],
            request.form['shield'],
            request.form['backpack'],
            request.form['bedroll']
        ]

        # Create a character object
        character = Character(name, race, class_, alignment, ability_scores, skills, equipment)

        # Save the character object to the database

        # Redirect to the character sheet
        return redirect(url_for('character_sheet', character_id=character.id))

# Define the character sheet route
@app.route('/character_sheet/<character_id>')
def character_sheet(character_id):
    # Retrieve the character object from the database
    character = Character.query.get(character_id)

    # Render the character sheet
    return render_template('character_sheet.html', character=character)

# Run the application
if __name__ == '__main__':
    app.run()
