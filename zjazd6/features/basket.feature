Feature: Adding product to basket on treenuts.pl

Scenario: Verify the process of adding a cream to the basket
    Given User is on the treenuts.pl website
    When User hovers over 'Sklep' and selects 'Kremy'
    Then User selects a specific cream and adds it to the basket
    And User verifies the basket value is '46,99 zł'
