do $$
-- Variables
-- Use same variable values as in resource.robot
declare
    test_user_1 varchar(50) := 'Felix';

-- pgsql commands
begin
    DELETE FROM users WHERE username = test_user_1;

end $$
