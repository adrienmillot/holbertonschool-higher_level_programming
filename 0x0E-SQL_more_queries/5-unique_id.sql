-- creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, name VARCHAR(256) NOT NULL);
ALTER TABLE unique_id ADD CONSTRAINT unique_id_constraint UNIQUE KEY(id);
