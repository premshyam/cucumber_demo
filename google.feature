# The feature which has to be tested
Feature: testing google url
# scenario
  Scenario: visit google and check
#    precondition
    Given we have behave installed
#   perform some action like visit a url you can replace http://www.google.com with the url of your choice
    When we visit "http://www.google.com"
#    observe outcomes like verify by checking the title of a page can replace Google with appropriate title
    Then it should have a title "Google"