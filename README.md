This Assignment is a Django based web application for managing the tasks assigned to the employees.
Has Navbar with 'employees', 'tasks' and 'todolist' options.

Models :
employee : Has employee related fields such as (emp id, emp name, email, dept, address)
task     : Has task related fields such as (task_id, task_name, member, priority, due_date etc), member is treated as ManytoMayField in order to
           maintain "Many to Many" relationship with employee table.

Urls:
Employees : http://localhost/emp/           : Provides details of the employees of the organization.
                                              Clicking on "add_employee" opens a form to fill employee details.

tasks     : http://localhost/tasks/         : Provides the task details (task_id, task_name, member, priority, due_date etc)
todolist  : https://tasks/actions/login/    : Opens a login page for the user (username- employee_name, password - empid),
                                              After login opens a page with following list of task actions.

                                            https://tasks/actions/create/    - Creates new task.
                                            https://tasks/actions/update/id  - Updates an existing task with the provided Id.
                                            https://tasks/actions/delete/id  - Deletes an existing task with the provided Id.
                                            https://tasks/actions/logout/    - Logout option if the user is already logged in.


                                  
                                  
