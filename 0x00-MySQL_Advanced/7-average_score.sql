-- 7-average_score.sql
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	UPDATE users
	SET
	average_score = (SELECT AVG(score) from corrections WHERE corrections.user_id = user_id)
	WHERE id = user_id;
END $$
DELIMITER ;
