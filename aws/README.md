### create_iam_user.py
The create_iam_user.py can be used in order to create a new IAM user (that needs to be assigned to
a given IAM role) - this script will also set a temporary password for the user (or if you choose to do
so, you can set the password to use yourself)

### Pre-requisites:
- For this script to work, you must ensure that you have the relevant AWS Access Key/Secret Access Key
combination exported and ready to use in your ~/.aws/credentials file.
- If you are using the aws-profile pip, ensure that you prefix the command to execute the script with 
"aws-profile -p envname"
- The IAM user (whom the access key combination belongs to) must have the relevant levels of access to create
a new IAM user

### Arguments:
create_iam_user.py takes the following arguments:
- -iam-group: The group to add the iam user to
- -iam-username: The username for the iam user to add
- -temp-password (Optional argument): Set the temporary password for the user - note that if this argument is
not supplied, the script will generate a random temporary password to assign to the user

### Execution:
To create an IAM user with a randomly generated temporary password, you would execute the following command (from the home dir of
this repository, replacing iamgroup with the iam group to assign the user to, and iamuser with the username for the iam user):

`python aws/create_iam_user.py -iam-group iamgroup -iam-username iamuser`

This will create the IAM user in the given account, generate and assign a temporary password (which is outputted so that it can be supplied to the user)
assigns this password to the user (whilst ensuring that upon logging in, the user must change their password) and then finally assigning the IAM user to
the relevant IAM group

To create an IAM user with a custom temporary password, you would execute the following command (from the home dir of
this repository, replacing iamgroup with the iam group to assign the user to, iamuser with the username for the iam user and temppassword
with the temporary password):

`python aws/create_iam_user.py -iam-group iamgroup -iam-username iamuser -temp-password temppassword`

This will create the IAM user in the given account, assigns the custom password to the user (whilst ensuring that upon logging in, the user must change their password) 
and then finally assigning the IAM user to the relevant IAM group

#### Notes:
- Remember to prefix either command with aws-profile -p envname if you are using the aws-profile pip
- You need to ensure that any temporary password conforms to the password conventions of the appropriate account

