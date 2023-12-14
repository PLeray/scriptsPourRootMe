import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adresse_serveur = ('localhost', 12345)
client_socket.connect(adresse_serveur)

# Envoyer des données au serveur
donnees_a_envoyer = "Bonjour, serveur!"
donnees_encodees = donnees_a_envoyer.encode("utf-8")
client_socket.send(donnees_encodees)

# ajout de /n al afin et sendall revoir chatgpt !!!!!!!!

# Recevoir la réponse du serveur
reponse_du_serveur = client_socket.recv(1024)
reponse_decodee = reponse_du_serveur.decode("utf-8")
print("Réponse du serveur :", reponse_decodee)

client_socket.close()