-- 9-index_name_score.sql
CREATE INDEX idx_name_first_score ON names (name(1), score);
