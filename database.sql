CREATE DATABASE IF NOT EXISTS transport_db;

USE transport_db;

CREATE TABLE IF NOT EXISTS transport_det (

    transport_id INT PRIMARY KEY AUTO_INCREMENT,

    source VARCHAR(50) NOT NULL,

    destination VARCHAR(50) NOT NULL,

    departure_time TIME NOT NULL,

    fare INT NOT NULL,

    transport_type VARCHAR(20) NOT NULL
);

-- -------------------- VELLORE --------------------

INSERT INTO transport_det
(source, destination, departure_time, fare, transport_type)
VALUES
('Chennai','Vellore','06:00:00',250,'Bus'),
('Chennai','Vellore','08:30:00',260,'Bus'),
('Chennai','Vellore','12:30:00',280,'Bus'),
('Chennai','Vellore','18:00:00',300,'Bus');

-- -------------------- BANGALORE --------------------

INSERT INTO transport_det
(source, destination, departure_time, fare, transport_type)
VALUES
('Chennai','Bangalore','07:00:00',600,'Bus'),
('Chennai','Bangalore','10:00:00',610,'Bus'),
('Chennai','Bangalore','13:00:00',620,'Bus'),
('Chennai','Bangalore','16:00:00',630,'Bus');

-- -------------------- COIMBATORE --------------------

INSERT INTO transport_det
(source, destination, departure_time, fare, transport_type)
VALUES
('Chennai','Coimbatore','06:30:00',550,'Bus'),
('Chennai','Coimbatore','09:30:00',560,'Bus'),
('Chennai','Coimbatore','12:30:00',570,'Bus'),
('Chennai','Coimbatore','15:30:00',580,'Bus');

-- -------------------- MADURAI --------------------

INSERT INTO transport_det
(source, destination, departure_time, fare, transport_type)
VALUES
('Chennai','Madurai','07:30:00',500,'Bus'),
('Chennai','Madurai','10:30:00',510,'Bus'),
('Chennai','Madurai','13:30:00',520,'Bus'),
('Chennai','Madurai','16:30:00',530,'Bus');

-- -------------------- TRICHY --------------------

INSERT INTO transport_det
(source, destination, departure_time, fare, transport_type)
VALUES
('Chennai','Trichy','08:00:00',450,'Bus'),
('Chennai','Trichy','11:00:00',460,'Bus'),
('Chennai','Trichy','14:00:00',470,'Bus'),
('Chennai','Trichy','17:00:00',480,'Bus');

-- -------------------- SALEM --------------------

INSERT INTO transport_det
(source, destination, departure_time, fare, transport_type)
VALUES
('Chennai','Salem','05:30:00',400,'Bus'),
('Chennai','Salem','09:00:00',420,'Bus'),
('Chennai','Salem','13:00:00',430,'Bus');

-- -------------------- ERODE --------------------

INSERT INTO transport_det
(source, destination, departure_time, fare, transport_type)
VALUES
('Chennai','Erode','06:15:00',480,'Bus'),
('Chennai','Erode','11:15:00',500,'Bus'),
('Chennai','Erode','16:15:00',520,'Bus');
