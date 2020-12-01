import argparse
import subprocess


def parse_arguments():
    description = "Arguments to be able to assign users to a role within a given space"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-o",
                        help="The name of the organisation for the space",
                        dest="org",
                        required=True)
    parser.add_argument("-remove-users",
                        help="Users to remove from the given role to (should be a comma separated list), off by default",
                        dest="remove_users",
                        default=False,
                        type=str,
                        required=False)
    parser.add_argument("-role",
                        help="The name of the role to assign users to/remove users from",
                        dest="role",
                        required=True)
    parser.add_argument("-s",
                        help="The name of the space to create",
                        dest="space",
                        required=True)
    parser.add_argument("-users",
                        help="The list of users to assign to/remove from given role to (should be a comma separated list)",
                        dest="users",
                        type=str,
                        required=True)
    return parser.parse_args()


# Backport for subprocess.run
def run(*popenargs, **kwargs):
    input = kwargs.pop("input", None)
    check = kwargs.pop("handle", False)

    if input is not None:
        if 'stdin' in kwargs:
            raise ValueError('stdin and input arguments may not both be used.')
        kwargs['stdin'] = subprocess.PIPE

    process = subprocess.Popen(*popenargs, **kwargs)
    try:
        stdout, stderr = process.communicate(input)
    except:
        process.kill()
        process.wait()
        raise
    retcode = process.poll()
    if check and retcode:
        raise subprocess.CalledProcessError(
            retcode, process.args, output=stdout, stderr=stderr)
    return retcode, stdout, stderr


def assign_user_to_role(org, role, space, user):
    try:
        run(['cf', 'set-space-role', user, org, space, role])
    except subprocess.CalledProcessError as e:
        print("Failed to create space: {}".format(e.output))


def remove_user_from_role(org, role, space, user):
    try:
        run(['cf', 'unset-space-role', user, org, space, role])
    except subprocess.CalledProcessError as e:
        print("Failed to create space: {}".format(e.output))


args = parse_arguments()
org = args.org
remove_users = args.remove_users
role = args.role
space = args.space
users = args.users
list_of_users = [user for user in users.split(',')]
if remove_users:
    for user in list_of_users:
        remove_user_from_role(org=org, role=role, space=space, user=user)
else:
    for user in list_of_users:
        assign_user_to_role(org=org, role=role, space=space, user=user)
