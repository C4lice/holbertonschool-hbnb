-- ===========================
-- 1. Insert Admin User
-- ===========================
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$HYYJi3aLy1CmW8jx70c8C.WWULt9oZG8yeGx02IsAcY.wwOCLPmqS',
    TRUE
);

-- ===========================
-- 2. Insert Initial Amenities
-- ===========================
INSERT INTO amenities (id, name) VALUES
    ('b1a2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d', 'WiFi'),
    ('c6d7e8f9-0a1b-4c2d-3e4f-5a6b7c8d9e0f', 'Swimming Pool'),
    ('d1e2f3a4-b5c6-4d7e-8f9a-0b1c2d3e4f5a', 'Air Conditioning');
