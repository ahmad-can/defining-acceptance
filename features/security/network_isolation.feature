Feature: Network Isolation
  As a cloud operator
  I want to verify network isolation between VMs and networks
  So that I can ensure proper security boundaries are enforced

  Background:
    Given the cloud is provisionned

  @security
  Scenario: Restricted network cannot reach external IPs
    Given a VM on the restricted network
    When I attempt to ping an external IP
    Then the connection should be blocked

  @security
  Scenario: Proxy filtering works
    Given a VM configured to use proxy
    When I make a web request
    Then the request should go through the proxy
