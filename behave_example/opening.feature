Feature: opening web site should show current todos

  Scenario: go to the web site, we arrive at the tasks page and there is a task list
     Given we have gone to the web site
      when we do nothing
      then we will be at the "Current Tasks" page
       and we will see a table with tasks in it
  
  Scenario: go to the web site, there is an "add item" row in the table
     Given we have gone to the web site
      when we do nothing
      then we will see a table with "Add another item..." row in it
       and every "Add another item..." row in the table has a link

  Scenario: go to the web site, there is an "add item" row in the table
     Given we have gone to the web site
      when we click on the first link in the "Add another item..." row
      then we will be at the "New Task" page

  @wip
  Scenario: when we're at the new task page, we will be able to create a task and see it in the list
     Given we have gone to the web site
      when we click on the first link in the "Add another item..." row
       and we enter input "Tell people not to enter stuff!" as new task
       and we click on button "save"
       and we click on the OK confirmation
      then we will be at the "Current Tasks" page
       and we will see a table with "Tell people not to enter stuff!" row in it



