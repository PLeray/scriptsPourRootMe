def complete_polybe_square(keyword):
    keyword = keyword.lower()  # Convertir le mot-clé en minuscules
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = "t-eo----m------s-d--p-a--"

    used_letters = set(keyword)

    # Construire une liste de lettres non utilisées (à l'exception de 'w')
    unused_letters = [letter for letter in alphabet if letter not in used_letters and letter != 'w']

    # Fusionner les lettres du mot-clé avec les lettres restantes
    #merged_letters = list(keyword) + unused_letters
    merged_letters = unused_letters + list(keyword) 

    # Créer un carré de Polybe 5x5 (sans le 'w')
    polybe_square = [merged_letters[i:i+5] for i in range(0, len(merged_letters), 5)]

    return polybe_square


def polybe_encrypt(plaintext,keyword):
    polybe_square = complete_polybe_square(keyword)


    ciphertext = ""
    for char in plaintext:
        if char == ' ':
            ciphertext += ' '  # Ajouter l'espace sans chiffrement
            continue

        if char == 'W':
            char = 'V'  # Remplacer 'W' par 'V'

        for i, row in enumerate(polybe_square):
            if char.upper() in row:
                col = row.index(char.upper()) + 1
                row_letter = chr(ord('a') + i)  # Convertir l'index en lettre
                ciphertext += row_letter + str(col)

    return ciphertext

def polybe_decrypt(ciphertext,keyword):
    polybe_square = complete_polybe_square(keyword)

    print("polybe_square:", polybe_square)
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        if ciphertext[i] == ' ':
            plaintext += ' '  # Ajouter l'espace sans déchiffrement
            i += 1
            continue


        row_letter = ciphertext[i]
        row = ord(row_letter) - ord('a') + 1  # Convertir la lettre en index
        col = int(ciphertext[i + 1])
        plaintext += polybe_square[row - 1][col - 1]
        i += 2

    return plaintext

# Exemple d'utilisation
keyword = ""

messageCrypte = "b4a4a1 d3a3 e1e3d1d1a3 e2b1a3b4d2a1 d2d4b3a3d1d1e3b4b4a3d4a1 e3 d1a4d4 a4b1a3d2c4c4a3"
messageCrypte = 'b3a3d1 c2b1e3d4d3d1 a4e5c5b1e3c2a3d1 b3a4b4e1e3b1a3d1 e3e5 b3a4b1e1d1 b2e5b4e3d2d4 d1a3b4c3c4a3d4a1'
decrypted_message = polybe_decrypt(messageCrypte,keyword)

print("Message d'origine:", messageCrypte)

print("Message déchiffré:", decrypted_message)


def decrypt_LeFichier(input_file, keyword):
    encrypted_lines = []
    with open(input_file, 'r') as file:
        for line in file.readlines():
            # Utilisez strip() pour supprimer les caractères de nouvelle ligne à la fin de chaque ligne
            encrypted_lines.append(line.strip())
   
    
    decrypted_lines = []

    i = 0
    ligne_dechiffre = ""
    for line in encrypted_lines:   
        while i < 1 : 
            print("ligne chiffré:", line) 
            ligne_dechiffre = polybe_decrypt(line, keyword)
            print("ligne déchiffré:", ligne_dechiffre) 
            #decrypted_lines.append(polybe_decrypt(line, keyword) + '\n')
            i += 1
            
    output_file = 'deCrypt-' + input_file
    with open(output_file, 'w') as file:
        file.writelines(decrypted_lines)

# Utilisation : remplacer 'input.txt' par le nom de votre fichier chiffré
# et 'output.txt' par le nom du fichier où vous souhaitez enregistrer le texte déchiffré.
decrypt_LeFichier('ch12.txt',keyword)