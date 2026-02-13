Feature: Access Control
  As a cloud operator
  I want to verify SSH access controls
  So that I can ensure only authorized users can access VMs

  Background:
    Given the cloud is provisionned

  @security
  Scenario: SSH with correct key succeeds
    Given a VM
    When I connect with correct SSH key
    Then the connection should succeed

  @security
  Scenario: SSH without key fails
    Given a VM
    When I connect without SSH key
    Then the connection should be refused
