-- Script to create a stored procedure ComputeAverageWeightedScoreForUsers

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN cur;

    -- Loop through each user
    user_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

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
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END //

DELIMITER ;
