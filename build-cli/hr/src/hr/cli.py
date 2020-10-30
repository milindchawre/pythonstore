from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()
    parser.add_argument("path", help="path to inventory file (JSON)")
    parser.add_argument("--export", action="store_true", help="export current settings to inventory file")
    return parser


def main():
    from hr import inventory, users

    parser = create_parser()
    args = parser.parse_args()
    if args.export:
        inventory.generate_inventory(args.path)
    else:
        user_dict = users.get_user_dict(args.path)
        existing_users = users.get_user_names()
        for user in user_dict:
            if user["name"] not in existing_users:
                users.create_user(user)
            elif user["name"] in existing_users:
                users.update_user(user)
        user_names = [user["name"] for user in user_dict]
        for user in existing_users:
            if user not in user_names:
                users.remove_user(user["name"])
