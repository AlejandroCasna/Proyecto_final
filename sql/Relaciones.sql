
CREATE DATABASE IF NOT EXISTS volleyball_database;
USE volleyball_database;

-- Tabla: equipo
CREATE TABLE IF NOT EXISTS equipo (
    id_equipo INT PRIMARY KEY,
    Equipo VARCHAR(255)
);


-- Tabla: jugadores
CREATE TABLE IF NOT EXISTS jugadores (
    Dorsal INT,
    Nombre VARCHAR(255),
    Posición VARCHAR(50),
    Altura FLOAT,
    Año_de_nacimiento INT,
    Alcance_en_ataque FLOAT,
    Alcance_en_bloqueo FLOAT,
    id_equipo INT,
    temporada VARCHAR(20),
    id_jugador INT PRIMARY KEY,
    FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo)
);

-- Tabla: receptor
CREATE TABLE IF NOT EXISTS receptor (
    Nombre VARCHAR(255),
    Partidos_jugados INT,
    Sets_jugados INT,
    Bloqueos INT,
    Bloqueo_exitoso INT,
    Bloqueo_fallido INT,
    Total_bloqueos INT,
    Saque INT,
    Errores_Saque INT,
    Porcentaje_error FLOAT,
    Total_saques INT,
    Ataque_exitoso INT,
    Errores_ataque INT,
    Porc_error FLOAT,
    Total_ataques INT,
    Ataque_Ranking INT,
    id_jugador INT PRIMARY KEY,
    temporada VARCHAR(20),
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
);

-- Tabla: opuesto
CREATE TABLE IF NOT EXISTS opuesto (
    Nombre VARCHAR(255),
    Partidos_jugados INT,
    Sets_jugados INT,
    Bloqueos INT,
    Bloqueo_exitoso INT,
    Bloqueo_fallido INT,
    Total_bloqueos INT,
    Saque INT,
    Errores_Saque INT,
    Porcentaje_error FLOAT,
    Total_saques INT,
    Ataque_exitoso INT,
    Errores_ataque INT,
    Porc_error FLOAT,
    Total_ataques INT,
    Ataque_Ranking FLOAT,
    id_jugador INT PRIMARY KEY,
    temporada VARCHAR(20),
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
);
-- Tabla: libero
CREATE TABLE IF NOT EXISTS libero (
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
    Recep_Ranking FLOAT,
    id_jugador INT PRIMARY KEY,
    temporada INT,
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
);

-- Tabla: colocador
CREATE TABLE IF NOT EXISTS colocador (
    Nombre VARCHAR(255),
    Partidos_jugados INT,
    Sets_jugados INT,
    Acciones_exitosas INT,
    Errores_colocador INT,
    _error_colocador INT,
    Puntos_negativos INT,
    Puntos_positivos INT,
    Acciones_positivas INT,
    Total_acumulado INT,
    Efic_Ranking INT,
    id_jugador INT PRIMARY KEY,
    temporada VARCHAR(20),
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
);

-- Tabla: jornadas
CREATE TABLE IF NOT EXISTS jornadas (
    fecha DATE,
    hora TIME,
    equipo_local VARCHAR(255),
    resultado VARCHAR(255),
    equipo_visitante VARCHAR(255),
    id_equipo_local INT,
    id_equipo_visitante INT,
    id_jornada INT,
    id INT PRIMARY KEY,
    FOREIGN KEY (id_equipo_local) REFERENCES equipo(id_equipo),
    FOREIGN KEY (id_equipo_visitante) REFERENCES equipo(id_equipo)
    );

-- Tabla: estadisticas_equipo



-- Tabla: clasificacion
CREATE TABLE IF NOT EXISTS clasificacion (
    Posición INT,
    Equipo VARCHAR(255),
    PJ INT,
    G INT,
    P INT,
    PTS INT,
    id_equipo INT PRIMARY KEY,
    temporada VARCHAR(20),
    FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo)
);

-- Tabla: centrales
CREATE TABLE IF NOT EXISTS centrales (
    Nombre VARCHAR(255),
    Partidos_jugados INT,
    Sets_jugados INT,
    Bloqueos INT,
    Bloqueo_exitoso INT,
    Bloqueo_fallido INT,
    Total_bloqueos INT,
    Saque INT,
    Errores_Saque INT,
    Porcentaje_error FLOAT,
    Total_saques INT,
    Ataque_exitoso INT,
    Errores_ataque INT,
    Porc_error FLOAT,
    Total_ataques INT,
    Ataque_Ranking INT,
    id_jugador INT PRIMARY KEY,
    temporada VARCHAR(20),
    FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
);

    CREATE TABLE IF NOT EXISTS temporada (
	id_temporada INT PRIMARY KEY,
    temporada VARCHAR (10)
    );
    
CREATE TABLE IF NOT EXISTS temporada_equipo (
    id_temporada INT,
    id_equipo INT,
    PRIMARY KEY (id_temporada, id_equipo),
    FOREIGN KEY (id_temporada) REFERENCES temporada(id_temporada),
    FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo)
    
);


CREATE TABLE IF NOT EXISTS clasificacion_2022 (
    Posición INT,
    Equipo VARCHAR(255),
    PJ INT,
    G INT,
    P INT,
    PTS INT,
    id_equipo INT PRIMARY KEY,
    temporada VARCHAR(20),
    FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo)
    );
    
    
CREATE TABLE IF NOT EXISTS estadisticas_temporada_anterior (
    Equipo VARCHAR(255),
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
    Efic_Saque FLOAT,
    Total_Recepcion INT,
    Error_Recepcion INT,
    Negativo_Recepcion INT,
    Positivo_Recepcion INT,
    Excelente_Recepcion INT,
    Efic_Recepcion FLOAT,
    Total_Ataque INT,
    Error_Ataque INT,
    Ataque_Bloqueado INT,
    Positivo_Ataque INT,
    Excelente_Ataque INT,
    Efic_Ataque FLOAT,
    Toque_Red_Bloqueo INT,
    Puntos_de_Bloqueo INT,
    Puntos_Set_Bloqueo INT,
    id_equipo INT PRIMARY KEY,
    temporada VARCHAR(20),
    FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo)
);




ALTER TABLE estadisticas_temporada_anterior
ADD COLUMN id_equipo_anterior INT,
ADD FOREIGN KEY (id_equipo_anterior) REFERENCES estadisticas_temporada_anterior(id_equipo);
