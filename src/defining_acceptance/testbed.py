from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExternalNetworks:
    external: str

    @classmethod
    def from_dict(cls, data: dict) -> "ExternalNetworks":
        external = data.get("external")
        if not isinstance(external, str) or not external.strip():
            raise ValueError("Machine external-networks.external must be a non-empty string")
        return cls(external=external)


@dataclass(frozen=True)
class MachineConfig:
    hostname: str
    ip: str
    osd_devices: str
    external_networks: ExternalNetworks
    fqdn: str | None = None
    role: str | None = None
    roles: list[str] | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "MachineConfig":
        hostname = data.get("hostname")
        ip = data.get("ip")
        osd_devices = data.get("osd-devices", "")

        if not isinstance(hostname, str) or not hostname.strip():
            raise ValueError("Machine hostname must be a non-empty string")
        if not isinstance(ip, str) or not ip.strip():
            raise ValueError(f"Machine '{hostname}' must include a non-empty ip")
        if not isinstance(osd_devices, str):
            raise ValueError(f"Machine '{hostname}' osd-devices must be a string")

        external_networks_raw = data.get("external-networks", {})
        if not isinstance(external_networks_raw, dict):
            raise ValueError(f"Machine '{hostname}' external-networks must be a mapping")

        fqdn = data.get("fqdn")
        if fqdn is not None and (not isinstance(fqdn, str) or not fqdn.strip()):
            raise ValueError(f"Machine '{hostname}' fqdn must be a non-empty string when set")

        role = data.get("role")
        if role is not None and (not isinstance(role, str) or not role.strip()):
            raise ValueError(f"Machine '{hostname}' role must be a non-empty string when set")

        roles = data.get("roles")
        if roles is not None:
            if not isinstance(roles, list) or not all(
                isinstance(item, str) and item.strip() for item in roles
            ):
                raise ValueError(
                    f"Machine '{hostname}' roles must be a list of non-empty strings"
                )

        return cls(
            hostname=hostname,
            ip=ip,
            osd_devices=osd_devices,
            external_networks=ExternalNetworks.from_dict(external_networks_raw),
            fqdn=fqdn,
            role=role,
            roles=roles,
        )


@dataclass(frozen=True)
class TestbedConfig:
    machines: list[MachineConfig]

    @classmethod
    def from_dict(cls, data: dict) -> "TestbedConfig":
        machines_raw = data.get("machines")
        if not isinstance(machines_raw, list) or not machines_raw:
            raise ValueError("Testbed must contain a non-empty machines list")

        machines: list[MachineConfig] = []
        for item in machines_raw:
            if not isinstance(item, dict):
                raise ValueError("Each machine entry in testbed must be a mapping")
            machines.append(MachineConfig.from_dict(item))

        return cls(machines=machines)
