Feature: Network Resilience
  As a cloud operator
  I want to verify network connectivity and DNS resolution
  So that I can ensure reliable network communication

  Background:
    Given the cloud is provisionned
    And all VMs are reachable via SSH

  @reliability
  Scenario: Network ACLs enforced
    Given a VM with restricted network access
    When I attempt to connect to a blocked IP
    Then the connection should be refused or timeout

  @reliability
  Scenario: DNS resolution works
    Given a running VM
    When I resolve external hostnames
    Then DNS resolution should succeed

  @reliability
  Scenario: Internal network communication
    Given multiple VMs on the same network
    When VMs communicate with each other
    Then the communication should succeed
