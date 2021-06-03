import json
import math

from core.models import User

from picklejar.settings import MASTER_KEY


def login(email, pass_data):
    grid_size = pass_data['grid_size']
    coords = pass_data['coords']
    user = User.objects.get(email=email)
    right_coords = decrypt_coords(user.passcoord)
    if _is_coords_correct(grid_size, coords, right_coords):
        return user
    return None


def signup(email, passimage_url, pass_data, first_name, last_name):
    grid_size = pass_data['grid_size']
    coords = pass_data['coords']
    coords = [(coord['x'] / grid_size, coord['y'] / grid_size) for coord in coords]
    User.objects.create(email=email, passcoord=encrypt_coords(coords), passimage_url=passimage_url,
                        first_name=first_name, last_name=last_name)


def _is_coords_correct(grid_size_px, coords_px, right_coords):
    coords = [(coord['x'] / grid_size_px, coord['y'] / grid_size_px) for coord in coords_px]

    finger_diameter_px = 40
    finger_diameter = finger_diameter_px / grid_size_px
    finger_radius = finger_diameter / 2

    for index in range(len(coords)):
        x, y = coords[index]
        max_x, min_x = x + finger_radius, x - finger_radius
        max_y, min_y = y + finger_radius, y - finger_radius

        right_x, right_y = right_coords[index]
        right_max_x, right_min_x = right_x + finger_radius, right_x - finger_radius
        right_max_y, right_min_y = right_y + finger_radius, right_y - finger_radius

        is_equal = x == right_x and y == right_y

        dx = min(max_x, right_max_x) - max(min_x, right_min_x)
        dy = min(max_y, right_max_y) - max(min_y, right_min_y)

        area_overlap = (dx >= 0) and (dy >= 0)

        if not is_equal and not area_overlap:
            return False
    return True


def _get_slot_by_coords(x, y, slot_size, grid_size):
    slot_coord_x = slot_coord_y = None
    for slot_number in range(1, int(math.ceil(grid_size / slot_size))):
        slot_value = slot_size * slot_number
        if slot_coord_x is None and x <= slot_value:
            slot_coord_x = slot_number
        if slot_coord_y is None and y <= slot_value:
            slot_coord_y = slot_number
        if slot_coord_y is not None and slot_coord_x is not None:
            break
    return slot_coord_x, slot_coord_y


def decrypt_coords(coords):
    return json.loads(MASTER_KEY.decrypt(coords.tobytes()))


def encrypt_coords(coords):
    return MASTER_KEY.encrypt(json.dumps(coords).encode())


def is_coords_valid(coords):
    is_valid = len(coords) == 5
    if is_valid:
        for coord in coords:
            if len(coord) != 2 or not isinstance(coord[0], int) or not isinstance(coord[1], int):
                return False
    return is_valid


def save_user(user_new_info, user):
    pass_data = user_new_info.get('pass_data')
    if pass_data:
        grid_size = pass_data['grid_size']
        coords = pass_data['coords']
        coords = [(coord['x'] / grid_size, coord['y'] / grid_size) for coord in coords]
        user.passcoord = encrypt_coords(coords)
    user.first_name = user_new_info['first_name']
    user.last_name = user_new_info['last_name']
    user.passimage_url = user_new_info['passimage_url']
    user.save()
