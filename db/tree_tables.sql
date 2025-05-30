CREATE TABLE tree_species(
    id SERIAL PRIMARY KEY, 
    common_name VARCHAR(100) NOT NULL,
    scientific_name VARCHAR(150) NOT NULL
);

CREATE TABLE trunk_structures(
    id SERIAL PRIMARY KEY,
    structure_type VARCHAR(100) NOT NULL
);

CREATE TABLE trees(
    id BIGSERIAL PRIMARY KEY,
    species INT NOT NULL,
    alcaldia VARCHAR(300) NOT NULL,
    colonia VARCHAR(300) NOT NULL,
    calle VARCHAR(500) NOT NULL,
    num VARCHAR(10) NOT NULL,
    cp VARCHAR(10) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    reference VARCHAR(500), 
    height FLOAT NOT NULL,
    base_diameter FLOAT NOT NULL,
    trunk_diameter FLOAT NOT NULL,
    crown_diameter FLOAT NOT NULL,
    trunk_inclination FLOAT NOT NULL,
    structure INT NOT NULL,
    health_status INT NOT NULL,
    last_inspection DATE,
    
    CONSTRAINT fk_species FOREIGN KEY (species) REFERENCES tree_species(id),
    CONSTRAINT fk_structure FOREIGN KEY (structure) REFERENCES trunk_structures(id)
);

CREATE TABLE tree_photos(
    id BIGSERIAL PRIMARY KEY,
    tree_id BIGINT NOT NULL,
    photo BYTEA NOT NULL,

    CONSTRAINT fk_tree FOREIGN KEY (tree_id) REFERENCES trees(id)
);

CREATE TABLE necessary_actions(
    id SERIAL PRIMARY KEY,
    tree_id BIGINT NOT NULL,
    action_description VARCHAR(255) NOT NULL,
    urgency INT NOT NULL CHECK (urgency BETWEEN 1 AND 5),
    cause_description VARCHAR(300) NOT NULL,

    CONSTRAINT fk_tree_actions FOREIGN KEY (tree_id) REFERENCES trees(id) 
);

CREATE TABLE health_statuses(
    id SERIAL PRIMARY KEY,
    tree_id BIGINT NOT NULL,
    condition VARCHAR(100) NOT NULL,

    CONSTRAINT fk_tree_health FOREIGN KEY (tree_id) REFERENCES trees(id)
);