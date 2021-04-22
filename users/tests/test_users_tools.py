#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from django.test import TestCase

from users.utilities import users_tools

""" Here are all our tools-tests which allows us to fill our database with json
files we dowloaded from 'Open Food facts API'. """

################################################################################
##                                  TESTS                                     ##
################################################################################

class TestViews(TestCase):

    def  setUp(self):
        """ We defined here all the datas we need to do our tests. """

        self.list_with_category_product = [
            {'id': 27, 'cat': 'comte', 'name': 'Bio Comté', 'brand': 'Monoprix, Monoprix Exploitation', 'store': 'Monoprix', 'nutriscore': 'c', 'fat_lipids_100g': '10', 'saturated_fatty_acids_100g': '6.6', 'sugar_100g': '0', 'salt_100g': '0.24', 'photo': 'https://static.openfoodfacts.org/images/products/335/003/366/4753/front_fr.38.400.jpg', 'link': 'https://fr-en.openfoodfacts.org/product/3350033664753/bio-comte-monoprix'},
            {'id': 187, 'cat': 'corn', 'name': 'Corn Flakes', 'brand': 'M-Budget,Migros', 'store': 'Migros', 'nutriscore': 'a', 'fat_lipids_100g': '1', 'saturated_fatty_acids_100g': '0.5', 'sugar_100g': '4', 'salt_100g': '0.975', 'photo': 'https://static.openfoodfacts.org/images/products/761/702/708/0224/front_fr.8.400.jpg', 'link': 'https://fr-en.openfoodfacts.org/product/7617027080224/corn-flakes-m-budget'},
            {'id': 140, 'cat': 'corn', 'name': 'Corn flakes', 'brand': "Kellogg's", 'store': 'Cora,Magasins U,Delhaize', 'nutriscore': 'c', 'fat_lipids_100g': '0.9', 'saturated_fatty_acids_100g': '0.2', 'sugar_100g': '8', 'salt_100g': '1.13', 'photo': 'https://static.openfoodfacts.org/images/products/315/947/000/0120/front_en.147.400.jpg', 'link': 'https://fr-en.openfoodfacts.org/product/3159470000120/corn-flakes-kellogg-s'},
            {'id': 362, 'cat': 'spaghetti', 'name': 'Fusilli', 'brand': 'Pasta mare,Bon et Bio', 'store': 'Aldi', 'nutriscore': 'a', 'fat_lipids_100g': '0.8', 'saturated_fatty_acids_100g': '0.2', 'sugar_100g': '1.4', 'salt_100g': '0.01', 'photo': 'https://static.openfoodfacts.org/images/products/26022314/front_fr.59.400.jpg', 'link': 'https://fr-en.openfoodfacts.org/product/26022314/fusilli-pasta-mare'},
            {'id': 386, 'cat': 'spaghetti', 'name': 'Spaghetti Cuisson Rapide', 'brand': 'U', 'store': 'Super U, Magasins U', 'nutriscore': 'a', 'fat_lipids_100g': '1.2', 'saturated_fatty_acids_100g': '0.3', 'sugar_100g': '3', 'salt_100g': '0.02', 'photo': 'https://static.openfoodfacts.org/images/products/325/622/572/0156/front_fr.41.400.jpg', 'link': 'https://fr-en.openfoodfacts.org/product/3256225720156/spaghetti-cuisson-rapide-u'},
            {'id': 701, 'cat': 'coppa', 'name': 'Coppa salé au sel sec', 'brand': 'Le Flutiau', 'store': 'Aldi', 'nutriscore': 'b', 'fat_lipids_100g': '6.7', 'saturated_fatty_acids_100g': '2.7', 'sugar_100g': '0', 'salt_100g': '0.2', 'photo': 'https://static.openfoodfacts.org/images/products/26026497/front_fr.19.400.jpg', 'link': 'https://fr-en.openfoodfacts.org/product/26026497/coppa-sale-au-sel-sec-le-flutiau'},
            {'id': 640, 'cat': 'coppa', 'name': 'Coppa', 'brand': 'Les Extra Fines du Forez', 'store': 'Carrefour', 'nutriscore': 'd', 'fat_lipids_100g': '11.5', 'saturated_fatty_acids_100g': '3.1', 'sugar_100g': '0.1', 'salt_100g': '3.83', 'photo': 'https://static.openfoodfacts.org/images/products/326/875/000/4045/front_fr.4.400.jpg', 'link': 'https://fr-en.openfoodfacts.org/product/3268750004045/coppa-les-extra-fines-du-forez'}
        ]

        return super().setUp()

    def test_parse_queryset(self):
        """ Here we make sure that there's at least one good product that matchs
        with our model fields in returning 'True'. In the wrong case it return
        'False' we can delete this file. """

        assert users_tools.parse_queryset(self.list_with_category_product) == ['comte', 'coppa', 'corn', 'spaghetti']
