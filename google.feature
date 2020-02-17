Feature: testing google

  Scenario: visit google and check
    When we visit "http://www.google.com"
    Then it should have a title "Google"