from conn import *
""" from datetime import datetime """

item_list = [
    ['item1', 99.95],
    ['item2', 599.95],
    ['item3', 1499.95],
    ['item4', 9999.95],
    ['item5', 99999.95]
]

vat_list = [
    ["AT", 20],  # Austria
    ["BE", 21],  # Belgium
    ["BG", 20],  # Bulgaria
    ["HR", 25],  # Croatia
    ["CY", 19],  # Cyprus
    ["CZ", 21],  # Czech Republic
    ["DK", 25],  # Denmark
    ["EE", 20],  # Estonia
    ["FI", 24],  # Finland
    ["FR", 20],  # France
    ["DE", 19],  # Germany
    ["GR", 24],  # Greece
    ["HU", 27],  # Hungary
    ["IE", 23],  # Ireland
    ["IT", 22],  # Italy
    ["LV", 21],  # Latvia
    ["LT", 21],  # Lithuania
    ["LU", 17],  # Luxembourg
    ["MT", 18],  # Malta
    ["NL", 21],  # Netherlands
    ["PL", 23],  # Poland
    ["PT", 23],  # Portugal
    ["RO", 19],  # Romania
    ["SK", 20],  # Slovakia
    ["SI", 22],  # Slovenia
    ["ES", 21],  # Spain
    ["SE", 25]  # Sweden
]

offer_list = [
    [1000, 3],
    [5000, 5],
    [7000, 7],
    [10000, 10],
    [50000, 15]
]

"""
# Define a formatted datetime
formatted_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
"""