-- create a stored procedure `ComputeAverageScoreForUser`
-- that computers and store the average score of a student.
DELIMITER $$ ;
CREATE PROCEDURE IF NOT EXISTS ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	UPDATE users SET average_score=(
		SELECT AVG(score) FROM corrections
		WHERE corrections.user_id=user_id
	)
	WHERE id=user_id;
END;$$
