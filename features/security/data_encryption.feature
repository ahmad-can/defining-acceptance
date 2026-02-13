Feature: Data Encryption
  As a cloud operator
  I want to verify data is encrypted in transit
  So that I can ensure data confidentiality and integrity

  Background:
    Given the cloud is provisionned

  @security
  Scenario: Internal network traffic is encrypted
    Given two VMs on internal network
    When I check network traffic
    Then traffic should be encrypted

  @security
  Scenario: External connections use TLS
    Given a VM with external service
    When I connect to the service
    Then TLS should be enforced
