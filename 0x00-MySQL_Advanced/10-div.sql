-- SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
-- You must create a function.
-- The function SafeDiv takes 2 arguments: a, INT and b, INT
-- returns a / b or 0 if b == 0

DELIMITER $$;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT AS BEGIN
  IF @b = 0
    RETURN 0
  ELSE
    RETURN CAST(a AS FLOAT) / b
END;$$
DELIMITER;
