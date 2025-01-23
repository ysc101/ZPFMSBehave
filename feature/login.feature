Feature: Login Action
  Scenario:Test the login page
    Given Launch Browser
    When User navigates to ZPFMS login Page
    Then User enters "<username>" and "<password>"
    Then User should get logged in
    And Message displayed Login Successfully

