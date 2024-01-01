Feature: Login to Swag Labs

  Scenario: Verify user login functionality
    Given User is on the login page
    When User enters valid credentials
    Then User should be redirected to the inventory page
