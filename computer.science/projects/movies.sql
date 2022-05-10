-- Create a table that has initially two columns: name and release year
CREATE TABLE films
(film_name TEXT, release_year INTEGER);

-- Add at least 10 records of your favorite movies into films table
INSERT INTO films
(film_name, release_year)
VALUES
('Parasite', 2019),
('The Intouchables', 2011),
('WALL-E', 2008),
('Joker', 2019),
('Toy Story', 1995),
('Soul', 2020),
('Finding Nemo', 2003),
('Monsters, Inc.', 2001),
('Ratatouille', 2007),
('Gandhi', 1982);

-- Look for all movies that were released when you were born
SELECT *
FROM films
WHERE release_year = 1995;

-- Add new columns: runtime_minutes, category, imdb_rating, box_office_earnings
ALTER TABLE films
ADD COLUMN runtime_minutes INTEGER,
ADD COLUMN category TEXT,
ADD COLUMN imdb_rating REAL,
ADD COLUMN box_office_earnings BIGINT
ADD COLUMN imdb_url;

-- Edit column name for box_office_earnings
ALTER TABLE films
RENAME COLUMN box_office_earnings TO worlwide_earnings;

-- Backfill runtime column with its respective data
UPDATE films
SET runtime_minutes = 132, category = 'Drama', imdb_rating = 8.5, worlwide_earnings = 258632621, imdb_url = 'https://www.imdb.com/title/tt6751668/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=EYG57T53MTCZ5RH46F1D&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_35' WHERE film_name = 'Parasite',
SET runtime_minutes = 112, category = 'Comedy', imdb_rating = 8.5, worlwide_earnings = 426588510, imdb_url = 'https://www.imdb.com/title/tt1675434/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=EYG57T53MTCZ5RH46F1D&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_44' WHERE film_name = 'The Intouchables',
SET runtime_minutes = 98, category = 'Animation', imdb_rating = 8.4, worlwide_earnings = 521311890, imdb_url = 'https://www.boxofficemojo.com/title/tt0910970/?ref_=bo_se_r_1' WHERE film_name = 'WALL-E',
SET runtime_minutes = 122, category = 'Crime', imdb_rating = 8.4, worlwide_earnings = 1074445730, imdb_url = 'https://www.imdb.com/title/tt7286456/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=EYG57T53MTCZ5RH46F1D&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_71' WHERE film_name = 'Joker',
SET runtime_minutes = 81, category = 'Animation', imdb_rating = 8.3, worlwide_earnings = 394436586, imdb_url = 'https://www.imdb.com/title/tt0114709/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=EYG57T53MTCZ5RH46F1D&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_75' WHERE film_name = 'Toy Story',
SET runtime_minutes = 100, category = 'Animation', imdb_rating = 8.0, worlwide_earnings = 120957731, imdb_url = 'https://www.imdb.com/title/tt2948372/?ref_=nv_sr_srsg_0' WHERE film_name = 'Soul',
SET runtime_minutes = 100, category = 'Animation', imdb_rating = 8.2, worlwide_earnings = 940352645, imdb_url = 'https://www.imdb.com/title/tt0266543/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=EYG57T53MTCZ5RH46F1D&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_154' WHERE film_name = 'Finding Nemo',
SET runtime_minutes = 92, category = 'Animation', imdb_rating = 8.1, worlwide_earnings = 579707738, imdb_url = 'https://www.imdb.com/title/tt0198781/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=EYG57T53MTCZ5RH46F1D&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_204' WHERE film_name = 'Monsters, Inc.',
SET runtime_minutes = 111, category = 'Animation', imdb_rating = 8.1, worlwide_earnings = 623726085, imdb_url = 'https://www.imdb.com/title/tt0382932/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=EYG57T53MTCZ5RH46F1D&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_223' WHERE film_name = 'Ratatouille',
SET runtime_minutes = 191, category = 'Drama', imdb_rating = 8.1, worlwide_earnings = 52767889, imdb_url = 'https://www.imdb.com/title/tt0083987/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=EYG57T53MTCZ5RH46F1D&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_245' WHERE film_name = 'Gandhi';

-- Add a constraint to film_name to allow unique values for this column
ALTER TABLE films
ADD CONSTRAINT unique_name UNIQUE (film_name);

-- View the current films table
SELECT *
FROM films;