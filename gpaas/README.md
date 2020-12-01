### assign_users_to_role.py
The assign_users_to_role.py script can be used in order to assign either a single or multiple users to a given role within
a GPaaS space. It is also possible to use this script in order to be able to remove a single or multiple users from a
given role

### Pre-requisites:
- The relevant organisation and space must already be present
- Your account must have permissions to assign users to roles in the relevant organisation and space
- You must have the CF CLI installed, and already be logged in to CF

### Arguments:
assign_users_to_role.py takes the following arguments:
- -o: The name of the organisation for the space
- -remove-users (Optional): Users to remove from the given role to (should be a comma separated list)
- -role: The name of the role to assign users to/remove users from
- -s: The name of the space to create
- -users: The list of users to assign to/remove from given role to (should be a comma separated list)

### Execution:
To assign a single user to a given role in gpaas, execute the following:

`python gpaas/assign_users_to_role.py -o organisationanem -s spacename -users user.name -role SpaceRole`

To assign multiple users to a given role in gpaas, execute the following (with users being passed in as a comma separated list:

`python gpaas/assign_users_to_role.py -o organisationanem -s spacename -users user.name1,user.name2 -role SpaceRole`

To remove a single user from a given role in gpaas, execute the following:

`python gpaas/assign_users_to_role.py -o organisationanem -s spacename -users user.name -role SpaceRole -remove-users yes`

To remove multiple users from a given role in gpaas, execute the following (with users being passed in as a comma separated list:

`python gpaas/assign_users_to_role.py -o organisationanem -s spacename -users user.name1,user.name2 -role SpaceRole -remove-users yes`