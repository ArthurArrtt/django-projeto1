from faker import Faker
from random import randint


def rand_ratio():
    return randint(80, 900), randint(473, 573)


fake = Faker("pt_BR")


def make_recipe():
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porcao',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://lorenflickr.com/%s/%s/food,cook' % rand_ratio()
        }
    }


if __name__ == "__main__":
    from pprint import pprint
    pprint(make_recipe())
