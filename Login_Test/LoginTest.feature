Feature: Login Test
  Scenario: Valid Creds
    Given Open a browser and navigate to "https://sikhinp-trials710.orangehrmlive.com"
    When Enter Valid Credentials: "Admin" and "ca@d01JOWR".
    Then Login should be successful
