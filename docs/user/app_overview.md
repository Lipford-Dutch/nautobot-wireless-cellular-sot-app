# App Overview

Nautobot Wireless Cellular SoT App manages cellular routers, SIM cards, carrier profiles, and normalized latest operational state.

Nautobot owns desired state. External collectors own high-frequency polling and historical telemetry.

## Alpha Rollout

- Roadmap discussion: [GitHub Discussion #2](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/discussions/2)
- Field reports and operator feedback: [GitHub Discussion #3](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/discussions/3)
- Standalone marketing page: [`cellular.html`](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/blob/main/cellular.html)
- UI sneak-peek screenshots: [`docs/media/ss_main_page_dark.png`](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/blob/main/docs/media/ss_main_page_dark.png) and [`docs/media/ss_main_page_light.png`](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app/blob/main/docs/media/ss_main_page_light.png)

## Operator Surfaces

- Dashboard: `/plugins/cellular-sot/`
- Cellular Routers: `/plugins/cellular-sot/cellular-routers/`
- SIM Cards: `/plugins/cellular-sot/sim-cards/`
- Carrier Profiles: `/plugins/cellular-sot/carrier-profiles/`
- Summary API: `/api/plugins/cellular-sot/summary/`
- Prometheus API: `/api/plugins/cellular-sot/prometheus/`
