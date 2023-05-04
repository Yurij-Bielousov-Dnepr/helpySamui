from django.utils.translation import gettext

TAG_ARTICLE_MOTO_RENT = 'moto_rent'
TAG_ARTICLE_MOTO_BEGINNER = 'moto_beginner'
TAG_ARTICLE_MOTO_SOS = 'moto_sos'
TAG_ARTICLE_RENT_ESTATE = 'rent_estate'
TAG_ARTICLE_PUBLIC_SERV = 'public_serv'
TAG_ARTICLE_LANG_SCHOL = 'lang_schol'
TAG_ARTICLE_MED_HELP = 'med_help'
TAG_ARTICLE_SERV_TRANSL = 'serv_transl'
TAG_ARTICLE_SHOPPING_DESTINATION = 'shopping_destination'
TAG_ARTICLE_SOUVENIRS = 'souvenirs'

TAG_ARTICLE_CHOICES = (
    (TAG_ARTICLE_MOTO_RENT, gettext("Moto Rent")),
    (TAG_ARTICLE_MOTO_BEGINNER, gettext("Moto Beginner")),
    (TAG_ARTICLE_MOTO_SOS, gettext("Moto SOS")),
    (TAG_ARTICLE_RENT_ESTATE, gettext("Rent Estate")),
    (TAG_ARTICLE_PUBLIC_SERV, gettext("Public Service")),
    (TAG_ARTICLE_LANG_SCHOL, gettext("Language School")),
    (TAG_ARTICLE_MED_HELP, gettext("Medical Help")),
    (TAG_ARTICLE_SERV_TRANSL, gettext("Translation Services")),
    (TAG_ARTICLE_SHOPPING_DESTINATION, gettext("Shopping Destination")),
    (TAG_ARTICLE_SOUVENIRS, gettext("Souvenirs")),
)
REVIEW_RATING_1_STAR = 1
REVIEW_RATING_2_STARS = 2
REVIEW_RATING_3_STARS = 3
REVIEW_RATING_4_STARS = 4
REVIEW_RATING_5_STARS = 5

REVIEW_RATING_CHOICES = (
    (REVIEW_RATING_1_STAR, gettext('1 star')),
    (REVIEW_RATING_2_STARS, gettext('2 stars')),
    (REVIEW_RATING_3_STARS, gettext('3 stars')),
    (REVIEW_RATING_4_STARS, gettext('4 stars')),
    (REVIEW_RATING_5_STARS, gettext('5 stars')),
)

TAG_HELP_MOTO_RENT = 'moto_rent'
TAG_HELP_MOTO_BEGINNER = 'moto_beginner'
TAG_HELP_MOTO_SOS = 'moto_sos'
TAG_HELP_RENT_ESTATE = 'rent_estate'
TAG_HELP_PUBLIC_SERV = 'public_serv'
TAG_HELP_LANG_SCHOL = 'lang_schol'
TAG_HELP_TRABL = 'trabl'
TAG_HELP_MED_HELP = 'med_help'
TAG_HELP_SERV_TRANSL = 'serv_transl'
TAG_HELP_SHOPPING_DESTINATION = 'shopping_destination'
TAG_HELP_CLOTHING = 'clothing'
TAG_HELP_FOOD = 'food'
TAG_HELP_SOUVENIRS = 'souvenirs'
TAG_HELP_IND_TOUR = 'ind_tour'
TAG_HELP_ESCORT = 'escort'

TAG_HELP_NAME_CHOICES = (
(TAG_HELP_MOTO_RENT, gettext("Moto Rent")),
(TAG_HELP_MOTO_BEGINNER, gettext("Moto Beginner")),
(TAG_HELP_MOTO_SOS, gettext("Moto SOS")),
(TAG_HELP_RENT_ESTATE, gettext("Rent Estate")),
(TAG_HELP_PUBLIC_SERV, gettext("Public Service")),
(TAG_HELP_LANG_SCHOL, gettext("Language School")),
(TAG_HELP_TRABL, gettext("Travel")),
(TAG_HELP_MED_HELP, gettext("Medical Help")),
(TAG_HELP_SERV_TRANSL, gettext("Translation Services")),
(TAG_HELP_SHOPPING_DESTINATION, gettext("Shopping Destination")),
(TAG_HELP_CLOTHING, gettext("Clothing")),
(TAG_HELP_FOOD, gettext("Food")),
(TAG_HELP_SOUVENIRS, gettext("Souvenirs")),
(TAG_HELP_IND_TOUR, gettext("Individual Tour")),
(TAG_HELP_ESCORT, gettext("Escort")),
)
REGION_CHOICES = [("", "Choose all"), ("Chaweng", "Chaweng"), ("Lamai", "Lamai"), ("Lipa Noi", "Lipa Noi"),
                  ("Nathon", "Nathon"), ("Bang Bor", "Bang Bor"), ("Maenam", "Maenam"), ("Bophut", "Bophut"),
                  ("Choeng Mon", "Choeng Mon"), ("Hua Thanon", "Hua Thanon"), ]

LANGUAGE_CHOICES = [("uk", "Українська"), ("th", "ไทย"), ("en", "English"), ("fr", "Français"), ("it", "Italiano"),
                    ("de", "Deutsch"), ("ru", "Русский"), ]

LEVEL_CHOICES = [(1, "Level 1"), (2, "Level 2"), (3, "Level 3"), ]

TAG_HELP_CHOICES = [("moto_rent", "Moto Rent"), ("moto_beginner", "Moto Beginner"), ("moto_sos", "Moto SOS"),
                    ("rent_estate", "Rent Estate"), ("public_serv", "Public Service"),
                    ("lang_schol", "Language School"), ("trabl", "Travel"), ("med_help", "Medical Help"),
                    ("serv_transl", "Translation Services"), ("shopping_destination", "Shopping Destination"),
                    ("clothing", "Clothing"), ("food", "Food"), ("souvenirs", "Souvenirs"),
                    ("ind_tour", "Individual Tour"), ("escort", "Escort"), ]
