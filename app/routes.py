from app import app
from flask import render_template, request
from .forms import PokemonForm
import requests 


@app.route('/')
def home():
    form = PokemonForm()
    return render_template ('base.html', form=form)

@app.route('/pokemon', methods=['GET','POST'])
def display_pokemon():
    form = PokemonForm()

    if form.validate_on_submit():
        pokemon_name = form.pokemon_name.data.lower()
        poke_info = get_data(pokemon_name)

        return render_template('pokemon.html', form=form, poke_info=poke_info)
    return render_template('pokemon.html', form=form)

@app.route('/pokemonlist')
def pokemonlist():
    form = PokemonForm()
    return render_template('pokemonlist.html', form=form, pokemon_list=[])

app.route('/nav')
def nav():
    form = PokemonForm()
    return render_template('nav.html', form=form)



def get_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    if response.ok:
        pokemon= response.json()
        poke_info = {
            'name': pokemon['species']['name'],
            'image_url': pokemon['sprites']['front_default'],
            'attack':pokemon['stats'][1]['base_stat'],
            'hp': pokemon['stats'][0]['base_stat'],
            'defense': pokemon['stats'][2]['base_stat'],
            'moves': pokemon['moves']
        }
        return poke_info