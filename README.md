Estructura de la Base de Datos

CREATE DATABASE Liga_Futbol;
USE Liga_Futbol;
CREATE TABLE admins (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE equipos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    director_tecnico VARCHAR(100) NOT NULL,
    partidos_jugados INT DEFAULT 0,
    victorias INT DEFAULT 0,
    empates INT DEFAULT 0,
    derrotas INT DEFAULT 0,
    goles_a_favor INT DEFAULT 0,
    goles_en_contra INT DEFAULT 0,
    puntos INT DEFAULT 0
);

CREATE TABLE jugadores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    posicion VARCHAR(50) NOT NULL,
    equipo_id INT NOT NULL,
    goles INT DEFAULT 0,
    asistencias INT DEFAULT 0,
    tarjetas_amarillas INT DEFAULT 0,
    tarjetas_rojas INT DEFAULT 0,
    minutos_jugados INT DEFAULT 0,
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
);

CREATE TABLE partidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    equipo_local INT NOT NULL,
    equipo_visitante INT NOT NULL,
    fecha DATE NOT NULL,
    marcador_local INT DEFAULT 0,
    marcador_visitante INT DEFAULT 0,
    admin_id INT NOT NULL,
    FOREIGN KEY (equipo_local) REFERENCES equipos(id) ON DELETE CASCADE,
    FOREIGN KEY (equipo_visitante) REFERENCES equipos(id) ON DELETE CASCADE,
    FOREIGN KEY (admin_id) REFERENCES admins(id) ON DELETE CASCADE
);

CREATE TABLE goles_partido (
    id INT PRIMARY KEY AUTO_INCREMENT,
    partido_id INT NOT NULL,
    jugador_id INT NOT NULL,
    minuto INT NOT NULL,
    FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE,
    FOREIGN KEY (jugador_id) REFERENCES jugadores(id) ON DELETE CASCADE
);
