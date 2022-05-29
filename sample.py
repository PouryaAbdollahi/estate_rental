from User import User
from random import choice
from region import Region
from advertisment import ApartmentSell, ApartmentRent, HouseRent, HouseSell

FIRST_NAMES = ['Milad', 'Zahra', 'Ali']
LAST_NAMES = ['Fatehi', 'Rezayi', 'Ahmadi']
PHONES = ['09148145710', '09017705901', '09034568792', '09108764983', '09017689125']


def create_sample():
    for mobile in PHONES:
        User(choice(FIRST_NAMES), choice(LAST_NAMES), mobile)

    reg1 = Region(name='region 1')
    reg2 = Region(name='region 2')

    apartment_sell = ApartmentSell(
        user=User.object_list[0], area=100,
        room_count=2, built_year=1400, region=reg1,
        address='lorem ipsum dolor ...', floor=2, has_parking=True, has_elevator=True,
        price_per_meter=10, discountable=True, convertable=False
    )

    apartment_rent = ApartmentRent(
        user=User.object_list[0], area=90,
        room_count=2, built_year=1400, region=reg1,
        address='lorem ipsum dolor ...', floor=2, has_parking=True, has_elevator=True,
        initial_price=1500, monthly_price=10, discountable=True, convertable=False
    )

    house_sell = HouseSell(
        user=User.object_list[-1], area=120, room_count=3,
        built_year=1395, region=reg2, address='lorem ipsum dolor ...',
        has_yard=True, floors_count=1,
        price_per_meter=1000, discountable=True, convertable=False
    )

    print('#' * 20, '\thello world\t', '#' * 20)

