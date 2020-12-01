import argparse
import random
import string
import subprocess


def parse_arguments():
    description = "Arguments to be able to create a space"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-iam-group",
                        help="The group to add the iam user to",
                        dest="iam_group",
                        required=True)
    parser.add_argument("-iam-username",
                        help="The username for the iam user to add",
                        dest="iam_username",
                        required=True)
    parser.add_argument("-temp-password",
                        help="Set the temporary password for the user (optional)",
                        dest="temp_password",
                        default=False,
                        required=False)
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


def create_iam_user(iam_username):
    try:
        run(['aws-profile', '-p', 'dfp-sandbox', 'aws', 'iam', 'create-user', '--user-name', iam_username])
    except subprocess.CalledProcessError as e:
        print("Failed to create space: {}".format(e.output))


def generate_iam_user_temp_password(iam_username):
    try:
        iam_user_temp_password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for _ in range(11))
        print("Temporary password for {}: {}".format(iam_username, iam_user_temp_password))
        return iam_user_temp_password
    except subprocess.CalledProcessError as e:
        print("Failed to create space: {}".format(e.output))


def create_iam_user_login_profile(iam_password, iam_username):
    try:
        run(['aws-profile', '-p', 'dfp-sandbox', 'aws', 'iam', 'create-login-profile', '--user-name', iam_username,
             '--password', iam_password, '--password-reset-required'])
    except subprocess.CalledProcessError as e:
        print("Failed to create space: {}".format(e.output))


def add_iam_user_to_group(iam_username, iam_group_name):
    try:
        run(['aws-profile', '-p', 'dfp-sandbox', 'aws', 'iam', 'add-user-to-group', '--user-name', iam_username,
             '--group-name', iam_group_name])
    except subprocess.CalledProcessError as e:
        print("Failed to create space: {}".format(e.output))


args = parse_arguments()
iam_group = args.iam_group
iam_username = args.iam_username
temp_password = args.temp_password
create_iam_user(iam_username=iam_username)
if temp_password:
    password = temp_password
else:
    password = generate_iam_user_temp_password(iam_username=iam_username)
create_iam_user_login_profile(iam_password=password, iam_username=iam_username)
add_iam_user_to_group(iam_username=iam_username, iam_group_name=iam_group)
