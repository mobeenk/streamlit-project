import socket
import getpass
import ldap3

# LDAP server settings
ldap_server = 'ldap://ldap_server_address:port'
ldap_user = 'username'
ldap_password = 'password'

# LDAP search settings
search_base = 'ou=users,dc=example,dc=com'  # Replace with the appropriate base DN

# Get the workstation name
workstation_name = socket.gethostname()

username = getpass.getuser()

ip_address = socket.gethostbyname(socket.gethostname())
print(workstation_name)
print(username)
#
# server = ldap3.Server(ldap_server)
# conn = ldap3.Connection(server, user=ldap_user, password=ldap_password)
# conn.bind()
#
# search_filter = f'(sAMAccountName={username})'
# conn.search(search_base, search_filter, attributes=['mail'])
# entries = conn.entries
#
# for entry in entries:
#     email = entry.mail.value
#     print(f"Workstation Name: {workstation_name}")
#     print(f"IP Address: {ip_address}")
#     print(f"Email Address: {email}")
#
#
# conn.unbind()
