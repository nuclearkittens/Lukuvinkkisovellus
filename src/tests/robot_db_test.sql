do $$
-- Variables
-- Use same variable values as in resource.robot
declare
    test_user_1 varchar(50) := 'Felix';
    test_title varchar(50) := 'Ajan luonne';
    test_title_2 varchar(50) := 'Gotrek & Felix';

-- pgsql commands
begin
    DELETE FROM books WHERE title = test_title;
    DELETE FROM books WHERE title = test_title_2;
    DELETE FROM users WHERE username = test_user_1;
end $$
