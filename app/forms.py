from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokemonForm(FlaskForm):
    pokemon_name = StringField('Enter Your Pokémon Character Name',validators=[DataRequired()])
    submit = SubmitField('Search')                          

