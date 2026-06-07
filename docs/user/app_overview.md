# App Overview

Nautobot Wireless Cellular SoT App manages cellular routers, SIM cards, carrier profiles, and normalized latest operational state.

Nautobot owns desired state. External collectors own high-frequency polling and historical telemetry.

## Operator Surfaces

- Dashboard: `/plugins/cellular-sot/`
- Cellular Routers: `/plugins/cellular-sot/cellular-routers/`
- SIM Cards: `/plugins/cellular-sot/sim-cards/`
- Carrier Profiles: `/plugins/cellular-sot/carrier-profiles/`
- Summary API: `/api/plugins/cellular-sot/summary/`
- Prometheus API: `/api/plugins/cellular-sot/prometheus/`
