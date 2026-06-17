"""GraphQL types for Nautobot Cellular SoT."""

from nautobot.core.graphql.types import OptimizedNautobotObjectType

from nautobot_cellular_sot.models import CarrierProfile, CellularOperationalSnapshot, CellularRouter, SIMCard


class CarrierProfileType(OptimizedNautobotObjectType):
    """GraphQL type for carrier profiles."""

    class Meta:
        model = CarrierProfile


class CellularRouterType(OptimizedNautobotObjectType):
    """GraphQL type for cellular routers."""

    class Meta:
        model = CellularRouter


class SIMCardType(OptimizedNautobotObjectType):
    """GraphQL type for SIM cards."""

    class Meta:
        model = SIMCard


class CellularOperationalSnapshotType(OptimizedNautobotObjectType):
    """GraphQL type for latest operational snapshots."""

    class Meta:
        model = CellularOperationalSnapshot


graphql_types = [CarrierProfileType, CellularRouterType, SIMCardType, CellularOperationalSnapshotType]
