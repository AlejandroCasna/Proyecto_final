-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS VolleyballDB;
USE VolleyballDB;

-- Tabla Equipo
CREATE TABLE Equipo (
    id_equipo VARCHAR(20) PRIMARY KEY ,
    Equipo VARCHAR(255) NOT NULL
);

-- Tabla Estadistica
CREATE TABLE Estadistica (
    id_estadistica INT PRIMARY KEY AUTO_INCREMENT,
    equipo VARCHAR(20),
    Jugados INT,
    Sets_Jugados INT,
    Total_Puntos INT,
    Break_Puntos INT,
    Puntos_Ganados INT,
    Puntos_Perdidos INT,
    Total_Saque INT,
    Puntos_Saque INT,
    Error_Saque INT,
    Puntos_por_set_Saque INT,
    Efic_Saque INT,
    Total_Recepcion INT,
    Error_Recepcion INT,
    Negativo_Recepcion INT,
    Positivo_Recepcion INT,
    Excelente_Recepcion INT,
    Efic_Recepcion INT,
    Total_Ataque INT,
    Error_Ataque INT,
    Ataque_Bloqueado INT,
    Positivo_Ataque INT,
    Excelente_Ataque INT,
    Efic_Ataque INT,
    Toque_Red_Bloqueo INT,
    Puntos_de_Bloqueo INT,
    Puntos_Set_Bloqueo INT,
    id_equipo VARCHAR(20),
    temporada VARCHAR(20),
    FOREIGN KEY (id_equipo) REFERENCES Equipo(id_equipo)
);

-- Tabla Clasificacion
CREATE TABLE Clasificacion (
    id_clasificacion INT PRIMARY KEY AUTO_INCREMENT,
    Posicion INT,
    equipo VARCHAR(50),
    PJ INT,
    G INT,
    P INT,
    PTS INT,
    id_equipo VARCHAR(50),
    temporada VARCHAR(50),
    FOREIGN KEY (id_equipo) REFERENCES Equipo(id_equipo)
);

-- Tabla Jornadas
CREATE TABLE Jornadas (
	ID iNT PRIMARY KEY AUTO_INCREMENT,
    id_jornada INT,
    fecha DATE,
    hora TIME,
    equipo_local VARCHAR(255),
    resultado VARCHAR(255),
    equipo_visitante VARCHAR(255),
    id_equipo_local VARCHAR(20),
    id_equipo_visitante VARCHAR(20),
    FOREIGN KEY (id_equipo_local) REFERENCES Equipo(id_equipo),
    FOREIGN KEY (id_equipo_visitante) REFERENCES Equipo(id_equipo)
);
fecha	hora	equipo_local	resultado	equipo_visitante	id_equipo_local	id_equipo_visitante	id_jornada
-- Tabla Jugadores
CREATE TABLE Jugadores (
    id_jugador VARCHAR(20) PRIMARY KEY,
    Dorsal INT,
    Nombre VARCHAR(255),
    Posicion VARCHAR(255),
    Altura INT,
    Ano_de_nacimiento INT,
    Alcance_en_ataque INT,
    Alcance_en_bloqueo INT,
    id_equipo VARCHAR(20),
    temporada VARCHAR(20),
    FOREIGN KEY (id_equipo) REFERENCES Equipo(id_equipo)
);

-- Tabla Opuesto
CREATE TABLE Opuesto (
    id_opuesto INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    Partidos_jugados INT,
    Sets_jugados INT,
    Bloqueos INT,
    Bloqueo_exitoso INT,
    Bloqueo_fallido INT,
    Total_bloqueos INT,
    Saque INT,
    Errores_Saque INT,
    Porcentaje_error INT,
    Total_saques INT,
    Ataque_exitoso INT,
    Errores_ataque INT,
    Porc_error INT,
    Total_ataques INT,
    Ataque_Ranking INT,
    id_jugador VARCHAR(20),
    id_equipo VARCHAR(20),
    temporada VARCHAR(20),
    FOREIGN KEY (id_jugador) REFERENCES Jugadores(id_jugador),
    FOREIGN KEY (id_equipo) REFERENCES Equipo(id_equipo)
);

-- Tabla Receptor
CREATE TABLE Receptor (
    id_receptor INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    Partidos_jugados INT,
    Sets_jugados INT,
    Bloqueos INT,
    Bloqueo_exitoso INT,
    Bloqueo_fallido INT,
    Total_bloqueos INT,
    Saque INT,
    Errores_Saque INT,
    Porcentaje_error INT,
    Total_saques INT,
    Ataque_exitoso INT,
    Errores_ataque INT,
    Porc_error INT,
    Total_ataques INT,
    Ataque_Ranking INT,
    id_jugador VARCHAR(20),
    id_equipo VARCHAR(20),
    temporada VARCHAR(20),
    FOREIGN KEY (id_jugador) REFERENCES Jugadores(id_jugador),
    FOREIGN KEY (id_equipo) REFERENCES Equipo(id_equipo)
);

-- Tabla Colocador
CREATE TABLE Colocador (
    id_colocador INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    Partidos_jugados INT,
    Sets_jugados INT,
    Acciones_exitosas INT,
    Errores_colocador INT,
    _error_colocador INT, -- Asegúrate de que sea el nombre correcto, puede ser un error tipográfico
    Puntos_negativos INT,
    Puntos_positivos INT,
    Acciones_positivas INT,
    Total_acumulado INT,
    Efic_Ranking INT,
    id_jugador VARCHAR(20),
    id_equipo VARCHAR(20),
    temporada VARCHAR(20),
    FOREIGN KEY (id_jugador) REFERENCES Jugadores(id_jugador),
    FOREIGN KEY (id_equipo) REFERENCES Equipo(id_equipo)
);

-- Tabla Central
CREATE TABLE Central (
    id_central INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    Partidos_jugados INT,
    Sets_jugados INT,
    Bloqueos INT,
    Bloqueo_exitoso INT,
    Bloqueo_fallido INT,
    Total_bloqueos INT,
    Saque INT,
    Errores_Saque INT,
    Porcentaje_error INT,
    Total_saques INT,
    Ataque_exitoso INT,
    Errores_ataque INT,
    Porc_error INT,
    Total_ataques INT,
    Ataque_Ranking INT,
    id_jugador VARCHAR(20),
    id_equipo VARCHAR(20),
    temporada VARCHAR(20),
    FOREIGN KEY (id_jugador) REFERENCES Jugadores(id_jugador),
    FOREIGN KEY (id_equipo) REFERENCES Equipo(id_equipo)
);

-- Tabla Libero
CREATE TABLE Libero (
    id_libero INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    Partidos_jugados INT,
    Sets_jugados INT,
    Recepciones INT,
    Recepciones_exitosas INT,
    Recepciones_fallidas INT,
    Recepciones_otro_jugador INT,
    Puntos_perdidos_recep INT,
    Puntos_ganados_recep INT,
    Total_puntos_recep INT,
    Recep_Ranking INT,
    id_jugador VARCHAR(20),
    id_equipo VARCHAR(20),
    temporada VARCHAR(20),
    FOREIGN KEY (id_jugador) REFERENCES Jugadores(id_jugador),
    FOREIGN KEY (id_equipo) REFERENCES Equipo(id_equipo)
);

