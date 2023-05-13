CREATE TABLE user (
    id_u INT PRIMARY KEY AUTO_INCREMENT,
    pseudo VARCHAR(40) UNIQUE NOT NULL,
    mdp VARCHAR(255) NOT NULL,
    nb_ville INT DEFAULT 0,
    date_creation_u DATETIME DEFAULT now()
);

CREATE TABLE ville (
    id_v INT PRIMARY KEY AUTO_INCREMENT,
    nom_ville VARCHAR(40) NOT NULL,
    date_creation_v DATETIME DEFAULT now(),
    aime INT DEFAULT 0,
    aime_pas INT DEFAULT 0,
    user INT NOT NULL,
    FOREIGN KEY(user) REFERENCES user(id_u)
);

CREATE TABLE objet (
    id_o INT PRIMARY KEY AUTO_INCREMENT,
    nom_objet VARCHAR(40) NOT NULL,
    longueur INT NOT NULL,
    largeur INT NOT NULL,
    description_objet text NOT NULL,
    type VARCHAR(20) NOT NULL,
    consomation FLOAT NOT NULL
);

CREATE TABLE ville_objet (
    id_ville INT,
    id_objet INT,
    PRIMARY KEY (id_ville, id_objet),
    FOREIGN KEY(id_ville) REFERENCES ville(id_v),
    FOREIGN KEY(id_objet) REFERENCES objet(id_o)
);

CREATE TABLE commentaire (
    id_c INT PRIMARY KEY AUTO_INCREMENT,
    date_c DATETIME DEFAULT now(),
    message TEXT NOT NULL,
    c_parent INT,
    user INT NOT NULL,
    ville INT NOT NULL,
    FOREIGN KEY(c_parent) REFERENCES commentaire(id_c),
    FOREIGN KEY(user) REFERENCES user(id_u),
    FOREIGN KEY(ville) REFERENCES ville(id_v)
);

INSERT INTO objet (nom_objet, longueur, largeur, description_objet, type, consomation) VALUES ('Lampadaire', 1, 1, "Permet d'éclairer la ville", "ELECTRIQUE", 23000 );
INSERT INTO objet (nom_objet, longueur, largeur, description_objet, type, consomation) VALUES ('Maison', 3, 3, "Habitat prévu pour 4 personnes", "LOGEMENT", 390);
INSERT INTO objet (nom_objet, longueur, largeur, description_objet, type, consomation) VALUES ("Immeubles", 6, 3,"Habitat prévu pour 64 personnes", "LOGEMENT", 600 );
INSERT INTO objet (nom_objet, longueur, largeur, description_objet, type, consomation) VALUES ("Champs solaire", 12, 9, "Espace permettant de produire de l'éléctricité grâce au soleil", "ELECTRIQUE", -0.20);
INSERT INTO objet (nom_objet, longueur, largeur, description_objet, type, consomation) VALUES ("Eolienne",1, 1, "Permet de réduire la consomation d'éléctricité", "ELECTRIQUE", 
-0.05 );
INSERT INTO objet (nom_objet, longueur, largeur, description_objet, type, consomation) VALUES ('Antenne 5G', 1, 1, 'Permet la communication entre téléphone', 'ELECTRIQUE', 19);
INSERT INTO objet (nom_objet, longueur, largeur, description_objet, type, consomation) VALUES ('Tramway', 2, 1, 'Moyen de transport sur rail', 'TRANSPORT', 125000000);
INSERT INTO objet (nom_objet, longueur, largeur, description_objet, type, consomation) VALUES ('Metro', 2, 1, 'Moyen de transport sous terrain', 'TRANSPORT', 200000000);
INSERT INTO objet (nom_objet, longueur, largeur, description_objet, type, consomation) VALUES ('Taxi autonome', 1, 1, 'Moyen de transport à des points fixes', 'TRANSPORT', 2112000);

-- USER ADMIN
INSERT INTO user (pseudo, mdp, nb_ville) VALUES ('admin', '$2y$10$uHZFejlooEWBjcmYV4VfnOfFpscb4BEjGyH6nIDhIs/tZdsZPI3Ka', 1);

-- VILLE ADMIN
INSERT INTO ville (nom_ville, user) VALUES ('VILLE ADMIN', 1);
