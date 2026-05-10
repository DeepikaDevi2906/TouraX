def get_places_tool(city):

    places_data = {

        "ooty": [

            "Botanical Garden",

            "Ooty Lake",

            "Doddabetta Peak",

            "Rose Garden"
        ],

        "chennai": [

            "Marina Beach",

            "Mahabalipuram",

            "Kapaleeshwarar Temple",

            "Vandalur Zoo"
        ],

        "coimbatore": [

            "Marudhamalai Temple",

            "Isha Foundation",

            "VOC Park"
        ],

        "kodaikanal": [

            "Kodai Lake",

            "Pillar Rocks",

            "Bryant Park"
        ]
    }


    return places_data.get(
        city.lower(),
        []
    )