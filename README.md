# P11_Cottenceau_Thomas
<h2>Nouvelle fonctionnalité de Pur-Beurre</h2>

<p>La nouveauté de cette plateforme est que désormais les substituts enregistrés par l'utilisateur dans son compte sont
groupés par categorie dans l'ordre alphabétique ce qui permet une bien meilleur visibilité.</p>

<h2>Who, When 'n' Why ?</h2>

<p>J'ai develloppé cette plateforme seul dans le cadre de ma formation OpenClassrooms du parcours 'developpeur d'applications Python' durant les mois de novembre à janvier 2021. Je suis ouvert à toute amélioration de votre part bien entendu si vous le désirez.</p>

<h2>Kesako ?</h2>

<p>Cette plateforme propose à un utilisateur de pourvoir substituer un produit qu'il consomme en vue d'en consommer un plus sain. Il peut s'il le désire ouvrir un compte afin d'y enregistrer ou de supprimer ses substitus.</p>

<h2>Installation</h2>

1. Pour l'installer, créez un dossier en local et clonez le projet 'P8_Cottenceau_Thomas' sur Github à l'adresse suivante :<br>
<em>https://github.com/thomsart/P8_Cottenceau_Thomas</em>

2. Une fois fait créez votre environnement virtuel et activez le :<br>
<em>python -m venv env</em> (pour le créer)<br>
<em>.\env\Scripts\activate</em> (pour l'activer)

3. Une fois activé installé y toutes les dépendances néccéssaires au projet en tapant la commande suivante :<br>
<em>pip install -r requirements.txt</em>

4. Créez votre base de données à l'aide de Postgrès. Pensez à bien modifier les paramètres liés à votre base de données dans les settings à l'url:<br>
<em>'startup_pur_beurre/settings/__init__.py'</em>

5. Maintenant il est temps de remplir la base de données en y entrant les produits que vous desirez, pour ce faire rendez vous sur l'API 'Open Food Facts' à cette adresse:
<em>https://fr.openfoodfacts.org/</em><br>
cherchez une categorie de produits qui vous intéresse et incluez la dans la liste 'category' présente dans fill_db.py<br>
Faites ensuite la commande suivante qui va se charger de les insérer en base de données :<br>
<em>python manage.py fill_db</em><br>

6. Une fois votre base de données bien remplis lancez le server avec la commande :<br>
<em>python manage.py runserver</em>

7. Enfin ouvrez votre navigateur web et tapez y la l'url suivante :<br>
<em>http://localhost:8000</em> (ici '8000' sur ma machine mais regardez le numéro du votre dans le terminal lors de l'activation de votre server.)

8. Il vous est possible de lancer les tests et le coverage (couverture des test) après amélioration de votre part en éxécutant les commandes suivantes:<br>
<em>pytest</em> (lance tout les tests des applications)<br>
Et pour avoir la couverture des tests faites:<br>
<em>pytest --cov=users</em> (pour l'application 'users')<br>
<em>pytest --cov=database</em> (pour l'application 'database')<br>

<h2>Liens de la plateforme sur le web</h2>

<p>Vous pouvez toute-fois vous rendre sur le site en ligne à cette adresse:<br>
<em>https://pur-beurre-cottenceau-thomas.herokuapp.com/</em></p>
<em>http://178.62.70.233/</em></p>
