-- Crear base de datos de coches y matriculas en postgresql
-- Crear tabla de gestores
CREATE TABLE gestores (
    id SERIAL PRIMARY KEY,
    gestor VARCHAR(50) NOT NULL,
    version VARCHAR(50) NOT NULL,
    caracteristicas VARCHAR(50) NOT NULL
);

-- Insertar datos

INSERT INTO gestores (gestor, version, caracteristicas) VALUES ('PostgreSQL', '9.5', 'Open Source');
INSERT INTO gestores (gestor, version, caracteristicas) VALUES ('MySQL', '5.7', 'Open Source');
INSERT INTO gestores (gestor, version, caracteristicas) VALUES ('Oracle', '12c', 'Propietario');
INSERT INTO gestores (gestor, version, caracteristicas) VALUES ('SQL Server', '2016', 'Propietario');

