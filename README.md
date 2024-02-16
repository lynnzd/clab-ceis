# clab-prototype

Repository dedicated to prototypes for the Circular Lab. Currently it consits of two _mocks_:
  
- CEIS: a the Circular Economy Information System
- A webshop: it interacts with the CEIS to get quote and register its orders

## How to run

```bash
docker compose build
docker compose up
```

Then connect to `http://localhost:8050` and `http://localhost:8051`

## Architecture

The overall idea is presented by the following diagram:

![alt text](doc/assets/overview.drawio.svg)