import plotly.express as px
import seaborn as sns

# Charger les données sur les passagers du Titanic (par exemple, avec Seaborn)
titanic_data = sns.load_dataset('titanic')

# Créer un graphique interactif avec Plotly
fig = px.scatter(titanic_data, x='age', y='fare', color='survived', hover_data=['sex', 'class'], 
                 title='Exploration des données sur les passagers du Titanic',
                 labels={'age': 'Âge', 'fare': 'Fare', 'survived': 'Survived'},
                 category_orders={'survived': ['No', 'Yes']})

# Afficher le graphique interactif
fig.show()
