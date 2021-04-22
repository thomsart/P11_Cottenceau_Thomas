#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################

"""
    This file contains all the functions create to do task we need in this
    application.

"""

################################################################################

def parse_queryset(list_of_saved_products):

    """
        this function takes in the queryset all the differentes categorys of
        product and put them in a list and finaly sort it alphabeticaly.
        If  
    """

    list_of_category = []
    for product in list_of_saved_products:
        for key, value in product.items():
            if key == 'cat':
                if value in list_of_category:
                    continue
                else:
                    list_of_category.append(product['cat'])
    list_of_category.sort()

    return list_of_category