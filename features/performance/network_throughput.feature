Feature: Network Throughput
  As a cloud operator
  I want to measure network performance between VMs
  So that I can validate network infrastructure meets requirements

  Background:
    Given the cloud is provisionned
    And all VMs are reachable via SSH

  @performance
  Scenario: Internal network throughput on same host
    Given two VMs on the same network and host
    When I measure throughput between them
    Then throughput should be at least 1 Gbps

  @performance
  Scenario: Internal network throughput on different host
    Given two VMs on the same network and different host
    When I measure throughput between them
    Then throughput should be at least 1 Gbps

  @performance
  Scenario: External network throughput
    Given a running VM
    When I download data from external source
    Then download speed should be acceptable