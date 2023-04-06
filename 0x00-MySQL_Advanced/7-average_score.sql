-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
-- An average score can be a decimal
-- ComputeAverageScoreForUser is taking 1 input which is user_id
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

drop procedure IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser(
        IN user_id INT
)
BEGIN
        UPDATE users
        SET average_score=(SELECT AVG(score) FROM corrections
                            WHERE corrections.user_id=user_id)
        WHERE id=user_id;
END;$$
DELIMITER ;
