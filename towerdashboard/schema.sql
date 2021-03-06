DROP TABLE IF EXISTS ansible_versions;
DROP TABLE IF EXISTS os_versions;
DROP TABLE IF EXISTS tower_versions;
DROP TABLE IF EXISTS tower_os;
DROP TABLE IF EXISTS tower_ansible;
DROP TABLE IF EXISTS results;

CREATE TABLE ansible_versions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  version TEXT UNIQUE NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE os_versions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  version TEXT UNIQUE NOT NULL,
  description TEXT UNIQUE NOT NULL,
  family TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tower_versions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  version TEXT UNIQUE NOT NULL,
  general_availability TEXT,
  end_of_full_support TEXT,
  end_of_maintenance_support TEXT,
  end_of_life TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tower_os (
  tower_id INTEGER NOT NULL,
  os_id INTEGER NOT NULL
);

CREATE TABLE tower_ansible (
  tower_id INTEGER NOT NULL,
  ansible_id INTEGER NOT NULL
);

CREATE TABLE results (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tower_id INTEGER NOT NULL,
  os_id INTEGER NOT NULL,
  ansible_id INTEGER NOT NULL,
  status TEXT,
  url TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
