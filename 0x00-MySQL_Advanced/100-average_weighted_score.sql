-- Script to create a stored procedure ComputeAverageWeightedScoreForUser

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;

    -- Calculate the total weighted score for the user
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        UPDATE users
        SET average_score = total_score / total_weight
        WHERE id = user_id;
    ELSE
        UPDATE users
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END //

DELIMITER ;
