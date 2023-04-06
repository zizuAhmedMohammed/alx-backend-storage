-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- That computes and store the average weighted score for a student.
-- ComputeAverageScoreForUser is taking 1 input which is user_id.
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT) AS 
BEGIN
  DECLARE weighted_score DECIMAL(5,2);
  SELECT weighted_score = SUM(score * weight) / SUM(weight)
  FROM grades
  WHERE user_id = user_id;
  UPDATE users SET average_score = @weighted_score WHERE id = user_id;
END;
